# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2859.0 Safari/537.36'
}


class URL(object):
    CITY_LIST = 'https://www.anjuke.com/sy-city.html'

    # 新房链接
    NEW_EMPTY_URL = 'https://{city}.fang.anjuke.com/loupan/all/p{page}/'
