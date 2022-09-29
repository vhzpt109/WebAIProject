import time as t
import requests
import datetime
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np

from google_images_download import google_images_download


if __name__ == "__main__":
    df_talent_list = pd.read_excel('./talent_list.xlsx', engine='openpyxl')
    talent_list = list(df_talent_list["name"])
    print(','.join(talent_list))

    response = google_images_download.googleimagesdownload()

    # keywords
    # limit : number of images
    # format
    arguments = {
        "keywords": "고양이",
        "limit": 1000,
        "print_urls": True,
        "chromedriver": "./libs/chromedriver",
        "format": "jpg"
        }

    # passing the arguments to the function
    paths = response.download(arguments)

    # printing absolute paths of the downloaded images
    print(paths)