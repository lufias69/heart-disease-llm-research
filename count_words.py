with open('JAMIA_SUBMISSION/Documents/MANUSCRIPT_FINAL.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract main sections
intro_start = content.find('## INTRODUCTION')
ack_start = content.find('## ACKNOWLEDGMENTS')

if intro_start > 0 and ack_start > intro_start:
    main_content = content[intro_start:ack_start]
    
    # Count total words (simple)
    total_words = len(main_content.split())
    
    # Estimate table content (roughly)
    table_lines = [line for line in main_content.split('\n') if '|' in line]
    table_words = sum(len(line.split()) for line in table_lines)
    
    # Net word count
    net_words = total_words - table_words
    
    print(f'Total words in sections: {total_words}')
    print(f'Estimated table words: {table_words}')
    print(f'Net main text words: {net_words}')
else:
    print('Could not find sections')
