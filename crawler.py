# -*- coding: utf-8 -*- 

import pandas as pd

from google_images_download import google_images_download

if __name__ == "__main__":
    # df_talent_list = pd.read_excel('./talent_list.xlsx', engine='openpyxl')
    # talent_list = list(df_talent_list["name"])
    # print(','.join(talent_list))

    response = google_images_download.googleimagesdownload()

    # keywords
    # limit : number of images
    # format
    arguments = {
        "keywords": "고양이",
        "limit": 10,
        "print_urls": True,
        "chromedriver": "./libs/chromedriver",
        "format": "jpg"
    }

    # passing the arguments to the function
    paths = response.download(arguments)

    # printing absolute paths of the downloaded images
    print(paths)