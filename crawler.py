import time as t
import requests
import datetime
from bs4 import BeautifulSoup
import csv

from google_images_download import google_images_download


if __name__ == "__main__":
    response = google_images_download.googleimagesdownload()

    # keywords
    # limit : number of images
    # format
    arguments = {
        "keywords": "Cat",
        "limit": 1000,
        "print_urls": True,
        "chromedriver": "./libs/chromedriver",
        "format": "jpg"
        }

    # passing the arguments to the function
    paths = response.download(arguments)

    # printing absolute paths of the downloaded images
    print(paths)