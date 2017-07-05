import re
import requests
import html
import time
from bs4 import BeautifulSoup


def crawl_joke_list_use_bs4(page=1):
    url = "http://www.qiushibaike.com/8hr/page/" + str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    joke_list = soup.find_all("div", class_="article block untagged mb15")
    for child in joke_list:
        print(child.find("h2").string + "\t" + "".join(child.find("div", class_="content").stripped_strings))
    time.sleep(1)


if __name__ == '__main__':
    crawl_joke_list_use_bs4(1)
