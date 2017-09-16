# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import time

import bs4
import requests

from anjuke_crawler.config import headers, URL


def getNewHousePrice(cityName):
    """
    :param cityName: 城市名英文缩写
    :return:获取该城市新房的当前价格
    """
    count = 1
    house = []
    url = URL.NEW_EMPTY_URL.format(city=cityName, page=count)
    while not til_end(url):
        time.sleep(2)
        req = requests.get(url=url, headers=headers)
        response = req.content

        soup = bs4.BeautifulSoup(response, 'lxml')
        data_list = soup.select('.item-mod')

        # TODO 逻辑待优化
        data = data_list[4:]
        # 获取楼盘名称
        for i in data:
            item_name = i.select('div[class="infos"] > div[class="lp-name"] > h3 > a')
            price = i.select('.favor-tag')
            price = price[0].get_text().strip() if len(price) > 0 else "null"
            lp_name = item_name[0].get_text()
            print({"lp_name": lp_name, "price": price})
            house.append({"lp_name": lp_name, "price": price})
        count += 1
        url = URL.NEW_EMPTY_URL.format(city=cityName, page=count)
    return house


def til_end(url):
    """
    judge current page is the end
    :param url:
    :return:
    """
    req = requests.get(url=url, headers=headers)
    response = req.content
    soup = bs4.BeautifulSoup(response, 'lxml')

    data_list = soup.select('.next-link')

    if len(data_list) > 0:
        return False
    else:
        return True
