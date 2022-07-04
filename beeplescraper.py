import bs4 as bs
import requests
import time
import random


# How do we determine when to stop requesting more pages?
# Answer: look for div with id='posts' and check if it is empty. Can do this
# using beautifulsoup.
#
# Get the post div using div = soup.find('div', attrs={'id': 'posts'}) and then
# check the length of its "children" using len(div.find_all())
# Or, could see if div.find_all() == []

MAX_PAGES = 300
PAGE_START = 1      # as of 2023 july 4, the last page is 282
SLEEP_TIME = 1      # seconds
DEBUG = True
WRITE = True        # If True, write the URLs to a text file


# We are going to add to this list when we loop through each HTML structure
hires_image_url_list = []

not_empty = True
max_pages = False
page_number = PAGE_START
while not_empty and not max_pages:

    if DEBUG:
        print('Requesting page {}.'.format(page_number))

    url = 'http://beeple.tumblr.com/page/{}'.format(page_number)
    r = requests.get(url)

    soup = bs.BeautifulSoup(r.text, 'html.parser')
    posts_div = soup.find('div', attrs={'id': 'posts'})
    not_empty = posts_div.find_all() != []

    if not_empty:
        if DEBUG:
            print('Got new posts. Appending...')

        for a in posts_div.find_all('img', attrs={'class': 'opacity-transition relative'}):
            hires_image_url_list.append(a['data-image-retina'])

    max_pages = page_number - PAGE_START + 1 >= MAX_PAGES

    page_number += 1

    sleep_time = SLEEP_TIME + random.randint(-500, 500) / 1000
    print('Sleeping for {:.3f} seconds...'.format(sleep_time))
    time.sleep(sleep_time)

if DEBUG:
    print('All done!')
    for x in hires_image_url_list:
        print(x)

if WRITE:
    if DEBUG:
        print('Writing image URLs to text file...')

    with open('image-urls.txt', 'w') as file:
        # TODO: there is probably better way to do this
        for x in hires_image_url_list:
            file.write(x + '\n')
