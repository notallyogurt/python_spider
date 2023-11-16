# -*- coding: utf-8 -*-
# @Time : 2023/9/14 13:18
# @Author : yogurt

import json
import pprint
import re
import time
import execjs
import requests

js = execjs.compile(open(r'./redbook.js', 'r', encoding='utf-8').read())

# q = js.call('get_xs','/api/sns/web/v2/comment/page?note_id=64ddde49000000000103ccaa&cursor=&top_comment_id=', '', '186ca73ccb9ht3l50qn35jga5z39zuv4j3l7i80a850000380091')
# print(q)


def requses_spider(url, method, headers=None, params=None,timeout=None,proxies=None, default=''):
    count = 0
    while True:
        try:
            res = getattr(requests, method)(url=url, headers=headers, params=params,proxies=proxies, timeout=timeout)
            break
        except Exception as e:
            if count > 4:
                print("程序请求异常次数过多请联系程序员 13217252129",default, e)
            time.sleep(2)
    return res

# 初始化请求，设置加密headers
def init(url, cookie):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'https://www.xiaohongshu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    headers['cookie'] = cookie
    # 获取加密 a1
    a1_list = re.findall('a1=(.*?);', cookie)
    # 获取url 加密参数
    encry_url = url.split('xiaohongshu.com')[-1]
    if a1_list:
        xs = js.call('get_xs', encry_url, '', a1_list[0])
        headers['x-s'] = xs['X-s']
    else:
        print("复制提供的cookie有错误请重新，复制cookie链接")
        exit()
    return headers
def flag_lenlist(list_data:list):
    if len(list_data):
        return list_data
    else:
        return False
def paser_talking(text,cookie, url):
    jsdata = json.loads(text)
    print(jsdata)
    list_save_data = []
    if jsdata['code'] == 0:
        first_comments =jsdata['data']['comments']
        if flag_lenlist(first_comments):
            for first_comment in first_comments:
                json_data = {}
                json_data['用户id'] = first_comment['id']
                json_data['ip地址'] = first_comment.get('ip_location')
                json_data['一级评论'] = first_comment['content']
                json_data['点赞人数'] = first_comment['like_count']
                json_data['评论人数'] = first_comment['sub_comment_count']
                if flag_lenlist(first_comment['sub_comments']):
                    list_sub = []
                    for sub_comment in first_comment['sub_comments']:
                        dict_sub = {}
                        dict_sub['用户id'] = sub_comment['id']
                        dict_sub['ip地址'] = sub_comment.get('ip_location')
                        dict_sub['二级用户评论'] = sub_comment['content']
                        dict_sub['点赞人数'] = sub_comment['like_count']
                        dict_sub['回复用户'] = sub_comment['target_comment']['id']
                        list_sub.append(dict_sub)
                    json_data['二级评论信息'] = list_sub
                list_save_data.append(json_data)
        # 打印输出存储数据
        pprint.pprint(list_save_data)
        print("cursor", jsdata['data']['cursor'])
        spider_title(url, cookie, jsdata['data']['cursor'])
    else:
        print("解析未能成功, 请尝试更换cookie后重试", jsdata)
        exit()


def spider_title(url, cookie, cursor):
    req_url = 'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id=' +url.split('/')[-1] + f'&cursor={cursor}&top_comment_id='
    print(req_url)
    # 获取帖子回复用户数据
    hearders = init(req_url, cookie)
    print(hearders['x-s'])
    text = requses_spider(req_url, 'get', headers=hearders).text
    paser_talking(text, cookie, url)




if __name__ == '__main__':

    url = "https://www.xiaohongshu.com/explore/64dbb998000000000b0282f4"
    cookie = "acw_tc=064f56ad72f8d9cdb7847c6d20367667f36d097feb36e9104025a9819f41acb1; abRequestId=3580adae-8b25-58cf-a420-addb927d0474; webBuild=3.10.6; xsecappid=xhs-pc-web; a1=18b12a2f127ov23rszma06l94hz8zlte73yqxusog50000376744; webId=05223878527e28a9f3f5ff2ff9c8413c; websectiga=2845367ec3848418062e761c09db7caf0e8b79d132ccdd1a4f8e64a11d0cac0d; gid=yYDyJ0Ji0yWiyYDyJ0Jiyq7MJWlhJqFMu608vlkK1j4xuA28Yu19dC888qWKW448SjqjKKY8; unread={%22ub%22:%2264f4014b000000001e00df56%22%2C%22ue%22:%226501be1b000000001f0063de%22%2C%22uc%22:29}; sec_poison_id=67307734-39f8-441b-a01d-ef9f62f4a36d; web_session=040069b2959d13cb7043ed3716374b347deda9"
    # 分类讨论
    if '/explore/' in url:
        spider_title(url, cookie, '')
    # spider_main(url, cookie)