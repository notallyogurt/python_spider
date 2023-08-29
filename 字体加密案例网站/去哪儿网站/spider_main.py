# -*- coding: utf-8 -*-
# @Time : 2023/8/28 16:45
# @Author : yogurt
import pprint
import re
import time

import requests
from fontTools.ttLib import TTFont
from lxml import etree

encry_dict = {
    '#1': '0',
    '#2': '1',
    '#3': '2',
    '#4': '3',
    '#5': '4',
    '#6': '5',
    '#7': '6',
    '#8': '7',
    '#9': '8',
    '#10': '9'
}


def return_encry(text, name):
    # 读取字体文件
    font = TTFont(f'{name}')
    cmap = font.getBestCmap()
    # print(cmap)
    str_1 = ""
    for item in list(text):
        try:
            item_1 = cmap[ord(item)]
            if item_1 == '*':
                a = encry_dict["#1"]
            else:
                code = '#' + str(int(item_1.split('#')[-1]) + 1)
                a = encry_dict[code]
        except:
            # 如果文字不在保存的字典中则让它存储原始值
            a = item
        str_1 += a

    return str_1


def reFirstdata(list_1):
    if len(list_1) > 0:
        return list_1[0].replace('\n', ' ').replace(' ', '').replace('\t', '')
    else:
        return ''


def requses_spider(url, method):
    count = 0
    while True:
        try:
            res = getattr(requests, method)(url=url)
            break
        except Exception as e:
            if count > 4:
                print("异常次数过多程序终止")
                exit()
            print(e)
            time.sleep(2)
    return res


def parser(name, text):
    tree = etree.HTML(text)
    li_list = tree.xpath('/html/body/div[1]/div[4]/div[1]/div/ul/li')
    list_data = []
    for item in li_list:
        title = reFirstdata(item.xpath('./div[1]/p[1]/a[1]//text()'))
        address = reFirstdata(item.xpath('./div[1]/p[1]/a[1]//text()'))
        grade = reFirstdata(item.xpath('./div[1]/p[3]/span//text()'))
        type = reFirstdata(item.xpath('./div[1]/p[4]/span//text()'))
        size = reFirstdata(item.xpath('./div[1]/p[5]//text()'))
        price = reFirstdata(item.xpath('./div[2]/div/span//text()'))
        price = return_encry(price, name)
        dict_1 = {
            'title': title,
            'address': address,
            'grade': grade,
            'type': type,
            'size': size,
            'price': price
        }
        # print(dict_1)
        list_data.append(dict_1)
    return list_data


def main(url):
    res = requses_spider(url, 'get')
    # print(res.text)
    # get woff_url
    woff_url = re.findall("url\('(.*?)'\) format\('woff'\),", res.text)[0]
    # down_load
    name = woff_url.split('?')[0].split('/')[-1]
    down_load_woff = requses_spider(woff_url, 'get')
    with open(f'{name}', 'wb') as f:
        f.write(down_load_woff.content)
    # 内容解析函数
    data = parser(name, res.text)
    pprint.pprint(data)
    return data


if __name__ == '__main__':
    url = "https://www.xuanzhi.com/yuanqu/page3"
    main(url)
