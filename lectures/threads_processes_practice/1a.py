"""
1. Create a script that download content over the network. The script should be able to
download web pages from a few sites, but it really could be any network traffic.
"""

import requests
import time

urls = ['https://google.com/',
        'https://uk.wikipedia.org/',
        'https://refactoring.guru/uk',
        'https://www.python.org/',
        'https://cursor.education/uk/'] * 50


# start = time.time()
# result = requests.get(urls[0])
# print(time.time() - start)
# print(result.text)


def download_site(url, session):
    with session.get(url) as response:
        print(f'Reading {len(response.content)} for {url}')


def download_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            download_site(url, session)


if __name__ == '__main__':
    start = time.time()
    download_all_sites(urls)
    print(f'Total Time for getting the content of {len(urls)} sites: {time.time() - start}')
