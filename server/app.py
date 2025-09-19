import os
import requests
import numpy as np
import cv2
app = Flask(__name__)
from flask_cors import CORS
CORS(app)


def get_image(url):
    """
    Fetch an image from a URL and print its shape using OpenCV.

    Args:
        url (str): URL of the image.

    Returns:
        tuple: Shape of the image (height, width, channels).
    """
    try:
        # Fetch the image from the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues

        img_array = np.asarray(bytearray(response.content), dtype=np.uint8)

        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if image is None:
            print("Error: Unable to decode the image.")
            return None
        return image

    except Exception as e:
        print(f"Error fetching or processing the image: {e}")
        return None