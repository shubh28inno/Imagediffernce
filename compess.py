import cv2
import os

# Paths
input_image_path = 'inimg/img3.jpg'
output_directory = 'difference_output'
max_size_kb = 100  # Maximum size in KB

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Read the image
img = cv2.imread(input_image_path)

# Initialize the compression parameters
compression_quality = 95  # Start with high quality
step = 5  # Quality decrement step

# Compress the image iteratively
while True:
    # Save the image to a temporary path with current compression
    temp_output_path = os.path.join(output_directory, 'temp.jpg')
    cv2.imwrite(temp_output_path, img, [cv2.IMWRITE_JPEG_QUALITY, compression_quality])

    # Check the size of the compressed image
    if os.path.getsize(temp_output_path) <= max_size_kb * 1024 or compression_quality <= step:
        break
    compression_quality -= step

# Final output path
output_path = os.path.join(output_directory, os.path.basename(input_image_path))

# Save the final image
os.rename(temp_output_path, output_path)
print(f"Compressed image saved at {output_path} with size {os.path.getsize(output_path) / 1024:.2f} KB")

# Delete the image if needed
# file_path = os.path.join(output_directory, os.path.basename(input_image_path))
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"Deleted image at {file_path}")
# else:
#     print(f"File {file_path} does not exist")
