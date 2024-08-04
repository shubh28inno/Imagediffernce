import cv2
import imutils
import numpy as np
import os
# from skimage.metrics import structural_similarity as compare_ssim

image1_path = './inimg/city1.jpg'
image2_path = './inimg/city2.jpg'


img1 = cv2.imread(image1_path)
img1=cv2.resize(img1,(600,360))
img2 = cv2.imread(image2_path)
img2=cv2.resize(img2,(600,360))

# Output folder for the difference image
diff_output_folder = 'difference_output'

gray1= cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
gray2= cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# (similar, diff)= compare_ssim(gray1, gray2, fu=True)

# diff=(diff*255).astype("uint8")
# cv2.imshow("Difference", diff)

diff= cv2.absdiff(gray1,gray2)
cv2.imshow("diff(img1,img2)",diff)

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# cv2.imshow("Threshold", thresh)

kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations=2)
cv2.imshow("Dilation", dilate)

 # Create output folder if it doesn't exist
os.makedirs(diff_output_folder, exist_ok=bool)

contours=cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# contours=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(contours)
if contours:
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(img1, (x,y), (x+w , y+h), (0, 0, 255), 2)
            cv2.rectangle(img2, (x,y), (x+w , y+h), (0, 0, 255), 2)

        # cv2.putText(img2, "Similarity:"+ str(similar), (10,30), cv2.FONT_HERSHEY_SIMPLEX, .7,(0,0,255), 2)
# Generate a filename based on the input image paths
#     filename = f"diff_{os.path.basename(image1_path)}"

#     # Save the difference image to the output folder
#     cv2.imwrite(os.path.join(diff_output_folder, filename), img1)

#     print(f"Differences found. Saved to {os.path.join(diff_output_folder, filename)}")
# else:
#     print("No differences found between the images.")


    x = np.zeros((360, 10, 3), np.uint8)
    result=np.hstack((img1, x, img2))
    cv2.imshow("Differences", result)

# Generate a filename based on the input image paths
    filename = f"diff_{os.path.basename(image1_path)}"

    # Save the difference image to the output folder
    cv2.imwrite(os.path.join(diff_output_folder, filename), result)
    # os.makedirs(diff_output_folder)

    # Example: result is set dynamically
    # result = result_path(diff_output_folder)  # Ensure this function returns a valid string path
    # if not isinstance(result, str):
    #     raise ValueError("The path must be a string.")
    if not os.path.exists(diff_output_folder):
        os.makedirs(diff_output_folder)
    file=f"temp_{os.path.basename(image1_path)}"
    temp_path = os.path.join(diff_output_folder, file)
    print(temp_path)
    cv2.imwrite(temp_path, result)
    # image=cv2.imread(temp_path)
    filepath=temp_path
    input_image_path = temp_path
    output_directory = 'compressed'
    max_size_kb = 100  # Maximum size in KB

    # os.remove(temp_path)

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
    output_path = os.path.join(output_directory, f"comp_{os.path.basename(input_image_path)}")

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

     

    # print(f"Differences found. Saved to {os.path.join(diff_output_folder, diff_output_folder)}")
else:
    print("No differences found between the images.")



# cv2.imshow("Original",img1)
# cv2.imshow("Edited", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()