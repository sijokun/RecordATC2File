from datetime import datetime
import subprocess as sp
import os

from lxml import etree
import requests


def get_raw_page(url: str) -> str:
    """
    Get raw page content
    :param url: url of the page
    :return: raw page content
    """
    r = requests.get(url)
    if r.status_code == 200:
        # print(r.text)
        return r.text
    else:
        raise ValueError(f'status_code for url {url} == {r.status_code}')


def get_winamp_link(url: str) -> str:
    """
    Get link from Winamp button
    :param url: url of stream
    :return: winamp link for stream
    """
    raw_page = get_raw_page(url)
    dom = etree.HTML(raw_page)
    winamp_link_xpath = '//td/a/@href'

    winamp_link = dom.xpath(winamp_link_xpath)[1]

    return winamp_link


def main():
    """
    main function
    :return:
    """
    base_link = os.environ['LINK']
    segment_time_in_seconds = os.environ['SEGMENT_TIME']

    while True:
        link = get_winamp_link(base_link)
        now = datetime.now()
        print(f'{now.strftime("%d_%m_%Y_%H_%M_%S")}: starting for link {link}')
        sp.run(['streamripper',
                link,
                '-d', './record',
                '-l', str(segment_time_in_seconds),
                '-a', f'{now.strftime("%d_%m_%Y_%H_%M_%S")}.mp3'])


if __name__ == '__main__':
    main()

