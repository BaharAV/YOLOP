###remove _mask
import os
import shutil

# Define source and destination directories
source_dir = '../dataset/mask/val'  # Change this to source directory
destination_dir = '../dataset/mask/val_2'  # Change this to destination directory

os.makedirs(destination_dir, exist_ok=True)

for filename in os.listdir(source_dir):
    # Check if the filename ends with '_mask.png'
    if filename.endswith('_mask.png'):
        # Create the new filename by removing '_mask' from the original
        new_filename = filename.replace('_mask', '')
        # Define full file paths
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, new_filename)
        # Copy the file to the destination directory with the new name
        shutil.copy2(source_file, destination_file)
        print(f"Copied and renamed: {filename} to {new_filename}")
print("All files have been processed.")
