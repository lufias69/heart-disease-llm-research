#!/usr/bin/env python3
"""Fix tree structure encoding errors in SUPPLEMENTARY_MATERIALS.md"""

import sys

# Read file
with open('e:/project/Riset/heart-disease/JAMIA_SUBMISSION/Documents/SUPPLEMENTARY_MATERIALS.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacements for tree structure characters
replacements = {
    # Box drawing characters that got corrupted
    '"œ"€"€': '├──',
    '"‚   ': '│   ',
    '"""€"€': '└──',
    # Smart quotes that might be in the original
    '"': '"',
    '"': '"',
    ''': "'",
    ''': "'",
}

# Apply replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Write back
with open('e:/project/Riset/heart-disease/JAMIA_SUBMISSION/Documents/SUPPLEMENTARY_MATERIALS.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print("Fixed tree structure encoding errors")
print("Replaced:")
for old, new in replacements.items():
    count = content.count(new)
    if count > 0:
        print(f"  '{old}' → '{new}' ({count} occurrences)")
