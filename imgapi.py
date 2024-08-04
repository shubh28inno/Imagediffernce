import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# Fetch the Image URL from 
def get_image_url():
    access_key = '45122305-ff67b78c9623bb9c382f1628b'  # Replace with your actual API access key
    url = f'https://pixabay.com/api/?key=45122305-ff67b78c9623bb9c382f1628b&q=yellow+flowers&image_type=photo&pretty=true{access_key}'
    response = requests.get(url)
    data = response.json()
    image_url = data['https://cdn.pixabay.com/user/2013/11/05/02-10-23-764_250x250.jpg']['regular']
    return image_url

# # Download and Display the Image
# def display_image(image_url):
#     response = requests.get(image_url)
#     img = Image.open(BytesIO(response.content))
#     plt.imshow(img)
#     plt.axis('off')  # Hide the axes
#     plt.show()

# Main Function
if __name__ == "__main__":
    image_url = get_image_url()
    # display_image(image_url)
