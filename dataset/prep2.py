##txt to png
import os
import cv2
import numpy as np

# Define directories
input_image_dir = '.../Golf_Cart_Dataset_Test'    # Update this path
input_txt_dir = '.../Golf_Cart_Dataset_Test'    # Update this path
output_dir = '.../Golf_Cart_Dataset_Test/mask_new'    # Update this path

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Function to create a mask for a single image
def create_mask(image_path, txt_path, output_path):
    # Original image resolution
    target_height, target_width = 720, 1280
    # Read the image to get its original dimensions
    image = cv2.imread(image_path)
    original_height, original_width = image.shape[:2]
    # Create an empty black mask with the original dimensions
    mask = np.zeros((original_height, original_width), dtype=np.uint8)
    # Read points from the text file
    points = []
    with open(txt_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 3:
                try:
                    x = float(parts[1])
                    y = float(parts[2])
                    points.append([x, y])
                except ValueError:
                    print(f"Warning: Could not convert line to float values: {line}")
    if not points:
        print(f"No valid points found in {txt_path}")
        return
    # Convert list of points to NumPy array
    points = np.array(points, dtype=np.float32)
    # Convert normalized coordinates to image pixel coordinates
    points[:, 0] *= original_width  # Scale x-coordinates
    points[:, 1] *= original_height # Scale y-coordinates
    # Convert to integers
    points = np.array(points, dtype=np.int32)
    # Ensure the points are in the required format for fillPoly
    if points.ndim == 1:
        points = points.reshape(-1, 1, 2)
    elif points.ndim == 2 and points.shape[1] == 2:
        points = points.reshape(1, -1, 2)
    # Draw the polygon on the mask
    cv2.fillPoly(mask, [points], 255)
    # Resize the mask to 720x1280
    resized_mask = cv2.resize(mask, (target_width, target_height), interpolation=cv2.INTER_NEAREST)
    # Save the resized mask image
    cv2.imwrite(output_path, resized_mask)
# Process each image and its corresponding text file
for image_filename in os.listdir(input_image_dir):
    if image_filename.endswith(('.png', '.jpg', '.jpeg')):  # Add other image extensions if needed
        image_path = os.path.join(input_image_dir, image_filename)
        txt_path = os.path.join(input_txt_dir, os.path.splitext(image_filename)[0] + '.txt')
        output_path = os.path.join(output_dir, image_filename)
        if os.path.exists(txt_path):
            create_mask(image_path, txt_path, output_path)
        else:
            print(f"Text file for {image_filename} not found.")
print("All masks created, resized to 720x1280, and saved successfully.")
