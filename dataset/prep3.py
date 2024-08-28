###resize png
import os
import cv2
# Define input and output directories
input_dir = '.../Golf_Cart_Dataset_Test'  # Update this path
output_dir = '.../Golf_Cart_Dataset_Test/img_new'  # Update this path
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Target resolution
target_height, target_width = 720, 1280
# Function to resize and save images
def resize_and_save_images(input_dir, output_dir, target_width, target_height):
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            # Construct the full file path
            img_path = os.path.join(input_dir, filename)
            # Read the image
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            # Resize the image to the target resolution
            resized_img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_LINEAR)
            # Construct the output path
            output_path = os.path.join(output_dir, filename)
            # Save the resized image
            cv2.imwrite(output_path, resized_img)
            print(f"Resized and saved: {filename}")
# Execute the resizing function
resize_and_save_images(input_dir, output_dir, target_width, target_height)
print("All PNG images resized and saved successfully.")