# -*- coding: utf-8 -*-
# @Time : 2023/8/29 15:55
# @Author : yogurt
import re
import time

import requests
from fontTools.ttLib import TTFont


def requses_spider(url, method, headers=None, params=None):
    count = 0
    while True:
        try:
            res = getattr(requests, method)(url=url, headers=headers, params=params)
            break
        except Exception as e:
            if count > 4:
                print("异常次数过多程序终止")
                exit()
            print(e)
            time.sleep(2)
    return res


def main(url):
    res = requses_spider(url, 'get')
    # downlode font
    font_url = re.findall('src:url\(&quot;(.*?)&quot', res.text)[0]
    font_res = requses_spider(font_url, 'get')
    with open('font.woff', 'wb') as f:
        f.write(font_res.content)
    font = TTFont('font.woff')
    cmap = font.getBestCmap()
    a = "\t".join(re.findall('font-G28BNCvDx6IvixLE">(.*?)<', res.text))
    dict_1 = {
        'gid58425': '0',
        'gid58700': '1',
        'gid58467': '2',
        'gid58525': '3',
        'gid58397': '4',
        'gid58385': '5',
        'gid58676': '6',
        'gid58347': '7',
        'gid58595': '8',
        'gid58461': '9',
        'gid58661': '年',
        'gid58378': '万'
    }
    str_1 = ""
    for item in list(a):
        # print(cmap[ord(item)])
        try:
            a = dict_1[cmap[ord(item)]]
        except:
            a = item
        str_1 += a
    print(str_1)


if __name__ == '__main__':
    url = "https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x"
    main(url)
