"""
Script untuk menganalisis struktur BAB 4 - HASIL DAN PEMBAHASAN
Memetakan semua sub bab, sub-sub bab, dan konten yang dibahas
"""

import re

def analyze_bab4_structure(filepath):
    """Analisis struktur heading dan konten BAB4"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract semua heading dengan level dan posisi
    heading_pattern = r'^(#{1,6})\s+(.+)$'
    lines = content.split('\n')
    
    structure = []
    current_section = None
    line_count = 0
    
    for i, line in enumerate(lines, 1):
        match = re.match(heading_pattern, line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            
            # Skip yang bukan struktur utama (level 1 duplikat)
            if level == 1 and 'BAB 4' not in title and i > 50:
                continue
                
            structure.append({
                'level': level,
                'title': title,
                'line_number': i,
                'line_count': 0
            })
            
            # Update line count untuk section sebelumnya
            if len(structure) > 1:
                structure[-2]['line_count'] = i - structure[-2]['line_number']
    
    # Update line count untuk section terakhir
    if structure:
        structure[-1]['line_count'] = len(lines) - structure[-1]['line_number']
    
    return structure, lines

def print_structure_tree(structure):
    """Print struktur dalam bentuk tree"""
    
    print("="*100)
    print("STRUKTUR HIERARKI BAB 4 - HASIL DAN PEMBAHASAN")
    print("="*100)
    print()
    
    bagian_counter = 0
    section_counters = [0, 0, 0, 0, 0, 0]  # untuk tracking numbering per level
    
    for item in structure:
        level = item['level']
        title = item['title']
        lines = item['line_count']
        
        # Reset counter untuk level di bawahnya ketika naik level
        for i in range(level, 6):
            section_counters[i] = 0
        
        # Increment counter untuk level ini
        if level <= 5:
            section_counters[level-1] += 1
        
        # Indentasi berdasarkan level
        indent = "  " * (level - 1)
        
        # Marker berdasarkan level
        if level == 1:
            marker = "[BAB]"
        elif level == 2:
            marker = "[2]"
            # Deteksi BAGIAN
            if 'BAGIAN' in title:
                bagian_counter += 1
        elif level == 3:
            marker = "[3]"
        elif level == 4:
            marker = "[4]"
        else:
            marker = "[5]"
        
        # Build numbering
        if level == 2 and not any(x in title for x in ['BAGIAN', '---', '===']):
            number = f"{section_counters[1]}"
        elif level == 3:
            number = f"{section_counters[1]}.{section_counters[2]}"
        elif level == 4:
            number = f"{section_counters[1]}.{section_counters[2]}.{section_counters[3]}"
        else:
            number = ""
        
        # Format output
        if 'BAGIAN' in title:
            print(f"\n{'='*100}")
            print(f"{marker} {title} (~{lines} baris)")
            print(f"{'='*100}\n")
        elif level == 1:
            print(f"\n{marker} {title}")
            print("-"*100)
        elif number and level >= 2:
            print(f"{indent}{marker} {number}. {title} ({lines} baris)")
        else:
            print(f"{indent}{marker} {title}")

def generate_detailed_mapping(structure, lines):
    """Generate detailed mapping dengan ringkasan konten"""
    
    print("\n\n")
    print("="*100)
    print("MAPPING DETAIL: TOPIK YANG DIBAHAS PER SEKSI")
    print("="*100)
    print()
    
    bagian = None
    
    for idx, item in enumerate(structure):
        level = item['level']
        title = item['title']
        start_line = item['line_number']
        line_count = item['line_count']
        
        # Skip metadata dan separator
        if any(x in title for x in ['---', '===', 'Penulis:', 'Institusi:', 'Tanggal:']):
            continue
        
        # Deteksi BAGIAN
        if 'BAGIAN' in title:
            bagian = title
            print(f"\n{'#'*100}")
            print(f"# {title}")
            print(f"{'#'*100}\n")
            continue
        
        # Hanya tampilkan level 2 dan 3 untuk detail
        if level in [2, 3]:
            # Extract preview konten (beberapa baris pertama setelah heading)
            preview_lines = []
            for i in range(start_line, min(start_line + 20, len(lines))):
                line = lines[i].strip()
                # Skip empty, heading, dan separator
                if line and not line.startswith('#') and not line.startswith('---') and not line.startswith('==='):
                    if not line.startswith('**') or line.count('**') >= 2:  # Allow full bold sentences
                        preview_lines.append(line)
                    if len(preview_lines) >= 3:
                        break
            
            indent = "  " * (level - 2)
            marker = "[2]" if level == 2 else "  [3]"
            
            print(f"{indent}{marker} {title}")
            print(f"{indent}   └─ {line_count} baris")
            
            if preview_lines:
                print(f"{indent}   └─ Topik:")
                for pline in preview_lines[:2]:
                    # Truncate jika terlalu panjang
                    if len(pline) > 120:
                        pline = pline[:117] + "..."
                    print(f"{indent}      • {pline}")
            print()

def generate_summary_stats(structure):
    """Generate statistik ringkasan"""
    
    print("\n")
    print("="*100)
    print("STATISTIK BAB 4")
    print("="*100)
    print()
    
    total_lines = sum(item['line_count'] for item in structure)
    
    # Count by level
    level_counts = {}
    for item in structure:
        level = item['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    # Count BAGIAN
    bagian_count = sum(1 for item in structure if 'BAGIAN' in item['title'])
    
    # Count sections (level 2, excluding BAGIAN)
    section_count = sum(1 for item in structure if item['level'] == 2 and 'BAGIAN' not in item['title'])
    
    print(f"Total baris konten: ~{total_lines:,}")
    print(f"Total BAGIAN utama: {bagian_count}")
    print(f"Total Seksi (##): {section_count}")
    print(f"Total Sub-seksi (###): {level_counts.get(3, 0)}")
    print(f"Total Sub-sub-seksi (####): {level_counts.get(4, 0)}")
    print()
    
    # Estimasi halaman (assuming ~50 lines per page with figures)
    estimated_pages = total_lines / 50
    print(f"Estimasi halaman: ~{estimated_pages:.0f} halaman")
    print()
    
    # Breakdown per BAGIAN
    print("Breakdown per BAGIAN:")
    print("-" * 60)
    
    current_bagian = None
    bagian_lines = 0
    
    for item in structure:
        if 'BAGIAN' in item['title']:
            if current_bagian:
                print(f"  {current_bagian}: ~{bagian_lines} baris (~{bagian_lines/50:.0f} hal)")
            current_bagian = item['title']
            bagian_lines = 0
        else:
            bagian_lines += item['line_count']
    
    # Print last bagian
    if current_bagian:
        print(f"  {current_bagian}: ~{bagian_lines} baris (~{bagian_lines/50:.0f} hal)")

def main():
    filepath = r'e:\project\Riset\heart-disease\skripsi\BAB4_HASIL_PEMBAHASAN.md'
    
    print("\nMenganalisis struktur BAB 4...")
    print("File:", filepath)
    print()
    
    structure, lines = analyze_bab4_structure(filepath)
    
    # 1. Print tree structure
    print_structure_tree(structure)
    
    # 2. Generate detailed mapping
    generate_detailed_mapping(structure, lines)
    
    # 3. Generate summary stats
    generate_summary_stats(structure)
    
    print("\n" + "="*100)
    print("ANALISIS SELESAI")
    print("="*100)

if __name__ == '__main__':
    main()
