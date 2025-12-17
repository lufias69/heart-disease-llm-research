"""
Database Module for LLM Testing Results
Purpose: Store predictions in SQLite with checkpoint capability
"""

import sqlite3
import pandas as pd
from datetime import datetime
import os


class ResultsDatabase:
    """
    SQLite database for storing LLM predictions with checkpoint support
    """
    
    def __init__(self, db_path='results/llm_predictions/predictions.db'):
        """
        Initialize database connection
        
        Args:
            db_path: Path to SQLite database file
        """
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
        print(f"✓ Database connected: {db_path}")
    
    def create_tables(self):
        """Create tables if they don't exist"""
        cursor = self.conn.cursor()
        
        # Main predictions table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_id INTEGER NOT NULL,
            run_id INTEGER NOT NULL,
            model TEXT NOT NULL,
            prediction TEXT,
            prediction_binary INTEGER,
            justification TEXT,
            raw_response TEXT,
            ground_truth INTEGER,
            timestamp TEXT NOT NULL,
            error TEXT,
            UNIQUE(test_id, run_id, model)
        )
        ''')
        
        # Experiment metadata table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS experiment_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total_samples INTEGER,
            runs_per_sample INTEGER,
            models TEXT,
            start_time TEXT,
            last_update TEXT,
            status TEXT
        )
        ''')
        
        # Progress tracking table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            model TEXT PRIMARY KEY,
            completed_predictions INTEGER,
            total_predictions INTEGER,
            last_test_id INTEGER,
            last_run_id INTEGER,
            last_update TEXT
        )
        ''')
        
        self.conn.commit()
        print("✓ Database tables ready")
    
    def save_prediction(self, test_id, run_id, model, prediction_result, ground_truth):
        """
        Save a single prediction to database
        
        Args:
            test_id: Test sample ID
            run_id: Run number (1-4)
            model: Model name (gpt, gemini, qwen)
            prediction_result: Dict with prediction, justification, etc.
            ground_truth: True label
        """
        cursor = self.conn.cursor()
        
        # Convert prediction to binary
        pred = prediction_result.get('prediction')
        if pred == 'Yes' or pred == 1:
            pred_binary = 1
        elif pred == 'No' or pred == 0:
            pred_binary = 0
        else:
            pred_binary = None
        
        try:
            cursor.execute('''
            INSERT OR REPLACE INTO predictions 
            (test_id, run_id, model, prediction, prediction_binary, justification, 
             raw_response, ground_truth, timestamp, error)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                test_id,
                run_id,
                model,
                pred,
                pred_binary,
                prediction_result.get('justification'),
                prediction_result.get('raw_response'),
                ground_truth,
                prediction_result.get('timestamp', datetime.now().isoformat()),
                prediction_result.get('error')
            ))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error saving prediction: {e}")
            return False
    
    def is_prediction_complete(self, test_id, run_id, model):
        """
        Check if a prediction already exists
        
        Args:
            test_id: Test sample ID
            run_id: Run number
            model: Model name
            
        Returns:
            bool: True if prediction exists
        """
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT COUNT(*) FROM predictions 
        WHERE test_id = ? AND run_id = ? AND model = ?
        ''', (test_id, run_id, model))
        
        count = cursor.fetchone()[0]
        return count > 0
    
    def get_progress(self, model):
        """
        Get progress for a specific model
        
        Args:
            model: Model name
            
        Returns:
            dict: Progress information
        """
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT completed_predictions, total_predictions, last_test_id, last_run_id
        FROM progress WHERE model = ?
        ''', (model,))
        
        row = cursor.fetchone()
        if row:
            return {
                'completed': row[0],
                'total': row[1],
                'last_test_id': row[2],
                'last_run_id': row[3],
                'percentage': (row[0] / row[1] * 100) if row[1] > 0 else 0
            }
        return None
    
    def update_progress(self, model, total_predictions, last_test_id=None, last_run_id=None):
        """
        Update progress for a model
        
        Args:
            model: Model name
            total_predictions: Total number of predictions expected
            last_test_id: Last completed test ID
            last_run_id: Last completed run ID
        """
        cursor = self.conn.cursor()
        
        # Count completed predictions
        cursor.execute('''
        SELECT COUNT(*) FROM predictions WHERE model = ?
        ''', (model,))
        completed = cursor.fetchone()[0]
        
        cursor.execute('''
        INSERT OR REPLACE INTO progress 
        (model, completed_predictions, total_predictions, last_test_id, last_run_id, last_update)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (model, completed, total_predictions, last_test_id, last_run_id, datetime.now().isoformat()))
        
        self.conn.commit()
    
    def get_all_predictions(self, model=None):
        """
        Get all predictions from database
        
        Args:
            model: Filter by model (optional)
            
        Returns:
            pd.DataFrame: All predictions
        """
        if model:
            query = 'SELECT * FROM predictions WHERE model = ? ORDER BY test_id, run_id'
            df = pd.read_sql_query(query, self.conn, params=(model,))
        else:
            query = 'SELECT * FROM predictions ORDER BY model, test_id, run_id'
            df = pd.read_sql_query(query, self.conn)
        
        return df
    
    def export_to_csv(self, model, output_path):
        """
        Export predictions to CSV
        
        Args:
            model: Model name
            output_path: Path to save CSV
        """
        df = self.get_all_predictions(model)
        df.to_csv(output_path, index=False)
        print(f"✓ Exported {len(df)} predictions to: {output_path}")
    
    def get_statistics(self):
        """
        Get overall statistics
        
        Returns:
            dict: Statistics
        """
        cursor = self.conn.cursor()
        
        stats = {}
        
        # Total predictions
        cursor.execute('SELECT COUNT(*) FROM predictions')
        stats['total_predictions'] = cursor.fetchone()[0]
        
        # By model
        cursor.execute('''
        SELECT model, COUNT(*) FROM predictions GROUP BY model
        ''')
        stats['by_model'] = {row[0]: row[1] for row in cursor.fetchall()}
        
        # Errors
        cursor.execute('SELECT COUNT(*) FROM predictions WHERE error IS NOT NULL')
        stats['errors'] = cursor.fetchone()[0]
        
        return stats
    
    def close(self):
        """Close database connection"""
        self.conn.close()
        print("✓ Database connection closed")
