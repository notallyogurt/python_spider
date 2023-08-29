# -*- coding: utf-8 -*-
# @Time : 2023/8/29 13:25
# @Author : yogurt
import re
import time

import requests
from fontTools.ttLib import TTFont
from lxml import etree

cookies = {
    '__mta': '245800635.1683545610394.1693286544268.1693286617491.12',
    '_lxsdk_cuid': '1851a31e01dc8-0c48e43478a2a7-26021e51-193530-1851a31e01dc8',
    'uuid_n_v': 'v1',
    'uuid': '6B76C3103E5D11EE867B4B88371CA499F70F77F0F3CF49E9B8C4C5590005AB69',
    '_lxsdk': '6B76C3103E5D11EE867B4B88371CA499F70F77F0F3CF49E9B8C4C5590005AB69',
    '_csrf': 'a4f0225ce9ff9e3499f76250e120311efd99ee23c012e4c6cf616b372db1bb09',
    'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1692428147,1693286521',
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1693287299',
    '_lxsdk_s': '18a3fbdd855-f78-373-a80%7C%7C13',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def requses_spider(url, method, headers=None, params=None):
    count = 0
    while True:
        try:
            res = getattr(requests, method)(url=url, headers=headers, params=params, cookies=cookies)
            break
        except Exception as e:
            if count > 4:
                print("异常次数过多程序终止")
                exit()
            print(e)
            time.sleep(2)
    return res


def reFirstdata(list_1):
    if len(list_1) > 0:
        return "".join(list_1).replace('\n', ' ').replace('  ', '').replace('\t', '')
    else:
        return ''


def encry_woff(camp, text):
    dict_encry = {
        'uniF66D': '0',
        'uniF615': '3',
        'uniE1B7': '8',
        'uniEC68': '2',
        'uniE5AC': '6',
        'uniE317': '7',
        'uniE274': '9',
        'uniEAB3': '4',
        'uniE6D5': '1',
        'uniEF74': '5',
        'uniEB19': '9',
        'uniE3EC': '2',
        'uniF7D2': '4',
        'uniED30': '1',
        'uniF3E8': '5',
        'uniF11C': '3',
        'uniEA60': '6',
        'uniEF28': '8',
        'uniEA6F': '0',
        'uniE3DF': '7',
        'uniE132': '7',
        'uniE83D': '5',
        'uniE583': '3',
        'uniEC4B': '9',
        'uniEBA2': '0',
        'uniE886': '2',
        'uniF23F': '6',
        'uniF16B': '4',
        'uniED8F': '1',
        'uniF05A': '8',
        'uniF7B3': '0',
        'uniED98': '9',
        'uniF70E': '6',
        'uniF0F0': '2',
        'uniED4F': '5',
        'uniE85F': '3',
        'uniE83F': '8',
        'uniE916': '7',
        'uniEDBA': '1',
        'uniEFE9': '4',
        'uniEB92': '7',
        'uniE8D7': '3',
        'uniF7FF': '6',
        'uniF85E': '1',
        'uniE99C': '2',
        'uniF1FC': '8',
        'uniF726': '0',
        'uniE8EE': '4',
        'uniE9EA': '9',
        'uniECDC': '5',

    }
    str_1 = ""
    list_1 = list(text)

    for item in list_1:
        try:
            a = dict_encry[camp[ord(item)]]
            # print(a)
        except:
            a = item
        str_1 += a

    return str_1


def parser(text):
    font = TTFont('font.woff')
    camp = font.getBestCmap()
    print(camp)
    tree = etree.HTML(text)
    div_list = tree.xpath('//*[@id="app"]/div/div[2]/div[2]/dl//dd')

    for item in div_list:
        # /div[1]/div[3]/a/div/div[1]
        # /div[1]/div[2]/a/div/div[1]
        name = reFirstdata(item.xpath('./div[1]/div[@class="movie-item-hover"]/a/div/div[1]//text()'))
        type = reFirstdata(item.xpath('./div[1]/div[@class="movie-item-hover"]/a/div/div[2]//text()'))
        autor = reFirstdata(item.xpath('./div[1]/div[@class="movie-item-hover"]/a/div/div[3]//text()'))
        time = reFirstdata(item.xpath('./div[1]/div[@class="movie-item-hover"]/a/div/div[4]//text()'))
        count = reFirstdata(item.xpath('./div[3]/span//text()'))
        count_1 = encry_woff(camp, count)
        print(name, type, autor, time, count_1)
    pass


def spider_main():
    params = (
        ('showType', '2'),
    )
    response = requses_spider('https://www.maoyan.com/films', 'get', headers=headers, params=params)
    url = 'https:' + re.findall(',url\("(.*)"\);\}', response.text)[0]
    woff = requses_spider(url, 'get')
    with open('font.woff', 'wb') as f:
        f.write(woff.content)

    parser(response.text)


if __name__ == '__main__':
    spider_main()
    # font = TTFont('font.woff')
    # camp = font.getBestCmap()
    # print(encry_woff(camp, "."))7621`/
