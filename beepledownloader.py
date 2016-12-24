import os
import requests
import random
import time

SLEEP_TIME = 2
MAX_IMAGES = 2000
DEBUG = True
WRITE_FOLDER = 'beeple_images'
IMAGE_URL_FILE = 'image-urls.txt'


def get_and_write(image_url):
    r = requests.get(image_url)

    image_name = os.path.basename(image_url)
    image_file_path = os.path.sep.join([WRITE_FOLDER, image_name])
    with open(image_file_path, 'wb') as image_file:
        image_file.write(r.content)


if __name__ == '__main__':
    if not os.path.exists(WRITE_FOLDER) and not os.path.isdir(WRITE_FOLDER):
        os.mkdir(WRITE_FOLDER)

    with open(IMAGE_URL_FILE, 'r') as url_file:
        image_number = 1
        for image_url in url_file:
            if image_number <= MAX_IMAGES:
                if DEBUG:
                    print(image_url)

                get_and_write(image_url.strip())

                image_number += 1

                sleep_time = SLEEP_TIME + random.randint(-500, 500) / 1000
                if DEBUG:
                    print('Sleeping for {:.3f} seconds...'.format(sleep_time))
                time.sleep(sleep_time)