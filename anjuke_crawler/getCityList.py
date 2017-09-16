# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import bs4
import requests

from anjuke_crawler.config import headers,URL


def getCityList():
    req = requests.get(url=URL.CITY_LIST, headers=headers)
    response=req.content
    soup = bs4.BeautifulSoup(response, 'lxml')

    data_list = soup.select('div[class="city_list"] > a')
    city_list = []
    for i in data_list:
        if isinstance(i, list):
            for j in i:
                city_list.append({"abbr":j['href'].split('.')[0][8:], "full":j.get_text()})
        else:
            city_list.append({"abbr":i['href'].split('.')[0][8:], "full":i.get_text()})

    return city_list

if __name__ == "__main__":
    for i in getCityList():
        print(i)
