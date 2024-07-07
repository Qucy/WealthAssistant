from PIL import Image
import numpy as np

def image_to_numpy_array(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to a numpy array
    numpy_array = np.array(image)

    return numpy_array

# Example usage
# image_path = 'C:\\Users\\tracy\\Downloads\\1718919859070.jpg'
# numpy_array = image_to_numpy_array(image_path)
# print(numpy_array)