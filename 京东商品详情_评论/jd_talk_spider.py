import json
import pprint
import re
import time
import requests

# 京东评论抓取文件
# ip 代理文件请更换代理以 确保程序运行
def getqG_json():
    url = "https://share.proxy.qg.net/get?key=8LYBGRUD&num=1&area=&isp=&format=json&seq=&distinct=true&pool=1"
    res = requests.get(url=url)
    js = json.loads(res.text)
    if js['code'] == 'SUCCESS':
        return {'http':"http://"+ js['data'][0]['server'], 'https':'http://' +  js['data'][0]['server']}
    else:
        return None

headers = {
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://item.jd.com',
    'Referer': 'https://item.jd.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'content-type': 'application/json;charset=gbk',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-referer-page': 'https://item.jd.com/100038222779.html',
    'x-rp-client': 'h5_1.0.0',
}
ip_proxie = getqG_json()

def dict_getvalue(dict_item, item, other=''):
    if dict_item.get(item):
        return dict_item[item]
    else:
        return f'暂无{other}数据'


def jd_talking(skuid):
    global ip_proxie
    list_page = []
    for count in range(0, 100):
        params = (
            ('appid', 'item-v3'),
            ('functionId', 'pc_club_skuProductPageComments'),
            ('client', 'pc'),
            ('clientVersion', '1.0.0'),
            ('t', '1696388191571'),
            ('loginType', '3'),
            ('uuid', '122270672.1695561279547644995890.1695561280.1696385255.1696397111.4'),
            ('productId', str(skuid)),
            ('score', '0'),
            ('sortType', '5'),
            ('page', count),
            ('pageSize', '10'),
            ('isShadowSku', '0'),
            ('fold', '1'),
            ('bbtf', ''),
            ('shield', ''),
        )

        while True:
            try:
                proxies = ip_proxie
                response = requests.get('https://api.m.jd.com/', headers=headers, params=params, timeout=5, proxies=proxies)
                # print(response.status_code)
                js = json.loads(response.text)
                break
            except Exception as e:
                print("商品评论获取失效，重新获取",ip_proxie, e)
                ip_proxie = getqG_json()

                time.sleep(1)
        goodRateShow = str(js['productCommentSummary']['goodRateShow']) + "%"
        if len(js['comments']) == 0:
            print("pagecount:", count, end= ' ')
            return list_page
        for Useritem in js['comments']:
            # 用户名
            username = dict_getvalue(Useritem, 'nickname').replace(r'\n', '').replace(r'\r', '').replace(',', '，')

            # plusAvailable
            plusAvailable = '暂无会员'
            if Useritem['plusAvailable'] == 201:
                plusAvailable = 'PLUS会员'

            # 评论内容
            content_1 = dict_getvalue(Useritem, 'content')
            ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
            content = ILLEGAL_CHARACTERS_RE.sub(r'', content_1).replace(r'\n', '').replace(r'\r', '').replace(',', '，').replace('\n', '').replace('\r', '')

            # 商品图片链接
            imgsrc = ''
            imgs = dict_getvalue(Useritem, 'images')

            if len(imgs) > 0 and '暂无' not in imgs:
                for img_url_item in imgs:
                    imgsrc += 'https:' + img_url_item['imgUrl'] + '\t'
            # 用户评分
            score = str(dict_getvalue(Useritem, 'score', '用户评分')) + "星"

            # 商品名称 sku
            productColor = dict_getvalue(Useritem, 'productColor', '商品详情').replace('\n', '').replace('\r', '').replace(',', '，')

            # 商品sku id
            referenceId = dict_getvalue(Useritem, 'referenceId', '商品sku').replace('\n', '').replace('\r', '').replace(',', '，') + '\t'

            # 评论创建时间
            creationTime = Useritem['creationTime'].replace('\n', '').replace('\r', '').replace(',', '，') + '\t'

            # 城市所在位置
            location = dict_getvalue(Useritem, 'location', '城市').replace('\n', '').replace('\r', '').replace(',', '，')

            # 评论点赞数
            usefulVoteCount = "点赞数" + str(Useritem['usefulVoteCount']).replace('\n', '').replace('\r', '').replace(',', '，')
            # '好评率, 用户名, 会员等级, 评论内容, 图片链接, 评分, 商品颜色, 商品sku, 评论创建时间, 城市所在位置, 评论点赞数'
            list_page.append(
                [goodRateShow, username, plusAvailable, content, imgsrc, score, productColor, referenceId, creationTime, location,
                 usefulVoteCount])
        # print(f"当前正在处理{skuid} 第 {count}页处理完成")
    return list_page

if __name__ == '__main__':
    list_data = jd_talking(236)
    pprint.pprint(list_data)
    print("len list_data", len(list_data))

