"""
Resize figures to meet JMIR maximum dimension requirements (1200x1200 pixels)
while maintaining aspect ratio and quality
"""

from PIL import Image
import os

# Source and destination folders
source_folder = r"E:\project\Riset\heart-disease\JAMIA_SUBMISSION\Figures"
dest_folder = r"E:\project\Riset\heart-disease\JMIR_SUBMISSION\Figures"

# Create destination folder if it doesn't exist
os.makedirs(dest_folder, exist_ok=True)

# Maximum dimension
MAX_DIM = 1200

# Process each figure
figures = ['Figure1.png', 'Figure2.png', 'Figure3.png']

for fig_name in figures:
    source_path = os.path.join(source_folder, fig_name)
    dest_path = os.path.join(dest_folder, fig_name)
    
    # Open image
    img = Image.open(source_path)
    original_size = img.size
    
    # Calculate new size maintaining aspect ratio
    width, height = img.size
    
    if width > height:
        # Landscape or square
        new_width = MAX_DIM
        new_height = int(height * (MAX_DIM / width))
    else:
        # Portrait
        new_height = MAX_DIM
        new_width = int(width * (MAX_DIM / height))
    
    # Resize with high quality
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Save with high quality
    resized_img.save(dest_path, 'PNG', optimize=True, quality=95)
    
    print(f"{fig_name}:")
    print(f"  Original: {original_size[0]} x {original_size[1]} pixels")
    print(f"  Resized:  {new_width} x {new_height} pixels")
    print(f"  Saved to: {dest_path}")
    print()

print("All figures resized successfully!")
print(f"\nResized figures saved in: {dest_folder}")
