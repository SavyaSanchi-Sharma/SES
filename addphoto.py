# setting dev key and cx
#gis = GoogleImagesSearch(os.getenv("GCS_DEVELOPER_KEY"), os.getenv("GCS_CX"))
import os
import glob
from pexels_api import API

# Ensure images directory exists
IMAGE_DIR = "./images/"
os.makedirs(IMAGE_DIR, exist_ok=True)

# Function to fetch and download images
# Function to empty the images folder
def get_images(query, n):
    client = API('5JV9cVZRTr6VUv9pqbYDWvxlluf7DvAtm1B8xL7VJvVia9ULckKbnYfc')  # Initialize API with key
    try:
        client.search(query)  # Perform search (no 'per_page' argument)
        photos = client.photos[:n]  # Get first 'n' photos

        if not photos:
            print(f"No images found for query: {query}")
            return []

        filenames = []
        for photo in photos:
            try:
                photo.download(IMAGE_DIR)
                filenames.append(os.path.join(IMAGE_DIR, os.path.basename(photo.original)))
            except Exception as e:
                print(f"Error downloading {photo.original}: {e}")

        return filenames
    except Exception as e:
        print(f"Error fetching images for query '{query}': {e}")
        return []
def empty_images():
    try:
        file_list = glob.glob(os.path.join(IMAGE_DIR, "*"))
        for file_path in file_list:
            os.remove(file_path)
        print("Image directory cleaned.")
    except Exception as e:
        print(f"Error cleaning image directory: {e}")

