import json
import os.path
import pprint
import random
import re
import time
import requests
from lxml import etree
from requests import RequestException

import ip_proxie
requests.packages.urllib3.disable_warnings()
headers = {
        'authority': 'api.m.jd.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'shshshfpa=e91e0034-e13c-0944-39b4-01489f965443-1695450863; shshshfpx=e91e0034-e13c-0944-39b4-01489f965443-1695450863; __jdu=1695561279547644995890; _pst=jd_62af11cd38106; unick=jd_62af11cd38106; pin=jd_62af11cd38106; _tp=1j6Ksjx5rAflR60J%2B3VIzuWjsDODT3plDjQt8BDk0TY%3D; thor=04807F69E56567D32E6F641A647410B909F14B267E2BE31C03177EB0846D296E7CFAFAAA4D0A834D82DA4F73872B7236724698A17BD162B58E0450822A922049612CC7C2EF357B5DB8F4F5C252CE687CB82CC1C3A17D81E0E200E30EF3F8A5ABEA20D8B4628E5FBC1D73F7E3B0B6C354CB3BDF4004E2C6DA863B0DFA5AA4C1EDDF8C47FA29AF3E405BF938BC608AD60FE31B15D9BF179CC97309EB785EBDCD71; flash=2_M079A1UMcwkRP3vlKvUU9cw3-gfeSQPOA5eA-IDqiJkEOOna8pOWSBfc1L45GXAE1Wdozhb_1buh18x6zCnlcFKVIcBqrJC6IDqpf4guhUK*; pinId=B_t2kVP0vYjKxe4Otrw_xrV9-x-f3wj7; unpl=JF8EAMhnNSttXh9RAE8DGBEZT1wBW1kMQkRTb2INUlpQS1YHSFVMFBR7XlVdXxRLFh9uYxRUXFNIUg4fBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwaFE9aVF1bAE8SBWhiAFxVXEJcBCsDKxUge21WXlwNQxczblcEZB8MF1QDHgIZG11LWlxaWQ9LFAVnYwBSWl1OXA0fCxMTIEptVw; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_7e44e022850d4558ba149769133bff75|1696472873758; PCSYCityID=CN_420000_420100_0; areaId=17; ipLoc-djd=17-1381-50712-62966; autoOpenApp_downCloseDate_jd_homePage=1696479418792_1; user-key=1b80f618-ddc7-4ed2-bbd9-d1f0d69384e1; cn=30; warehistory="100066896214,100066896214,100066896214,"; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1696484055015_1; 3AB9D23F7A4B3CSS=jdd034TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBYAAAAMK73RIPJIAAAAACZ67XBY52GUDBMX; joyya=1696493373.1696493378.23.0dfqyrg; jsavif=1; __jda=122270672.1695561279547644995890.1695561280.1696483301.1696493371.9; __jdc=122270672; token=bdcdb22f9c5ea357c373b76cd520739c,3,942496; __tk=ff0b1a66335af2e7a78cd5ee7abe0b02,3,942496; 3AB9D23F7A4B3C9B=4TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBY; shshshsID=ba15b147c5ab32c484f608a760771220_6_1696493429942; shshshfpb=AAm1r4_6KEh4ANOE8CUQ5tAFIn5ZUQxaVRQhjfwAAAAA; __jdb=122270672.5.1695561279547644995890|9.1696493371',
        'origin': 'https://item.jd.com',
        'referer': 'https://item.jd.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-referer-page': 'https://item.jd.com/100066896214.html',
        'x-rp-client': 'h5_1.0.0',
    }


proxie_1 = ip_proxie.getqG_json()
def base_spider(headers, params, cookies):
    # print(cookies)
    global proxie_1
    test_count = 0

    while True:
        proxie = proxie_1
        try:
            # print(params, end=' \t')
            response = requests.get('https://api.m.jd.com/', headers=headers, params=params, proxies=proxie,cookies=cookies, timeout=4,
                                    verify=False)
            if response.status_code != 403:
                if json.loads(response.text).get('code') == '605':
                    time.sleep(5)
                    proxie_1 = ip_proxie.getqG_json()
                    raise RuntimeError('605')
                js = json.loads(response.text)
                if js is None:
                    raise RuntimeError("请求页面无数据")
                return js
            else:
                time.sleep(5)
                raise RuntimeError('403')
        except RequestException as e:
            print(proxie)
            time.sleep(3)
            print('http error 重新跟换代理请求')
            proxie_1 = ip_proxie.getqG_json()
        except Exception as e:
            time.sleep(3)
            if test_count > 3:
                print('http error 重新跟换代理请求')
                proxie_1 = ip_proxie.getqG_json()
            test_count += 1
            print("商品详情获取失败重新获取", e, proxie, response.text)




def h5st_rquests(sku, cookies):
    headers['x-referer-page'] = f'https://item.jd.com/{sku}.html'

    params = {
        'appid': "pc-item-soa",
        'functionId': "pc_detailpage_wareBusiness",
        'client': "pc",
        'clientVersion': "1.0.0",
        't': int(time.time()),
        'body': '{"skuId":' + str(sku)+ ',"cat":"9987,653,655","area":"17_1381_50712_62966","shopId":"1000000127","venderId":1000000127,"paramJson":"{\\"platform2\\":\\"1\\",\\"specialAttrStr\\":\\"p0ppppppppp2p1ppppppppppppp3p\\",\\"skuMarkStr\\":\\"00\\"}","num":"1","bbTraffic":""}',
        # 'x-api-eid-token': 'jdd034TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBYAAAAMLCKN56UIAAAAACTPUQK4RONYC7EX',

    }

    res = requests.get("http://127.0.0.1:8080/get", params={'text':json.dumps(params)})

    data_param = dict(params,**json.loads(res.text))
    res = requests.get("http://127.0.0.1:8080/get_token", params={'sku': sku})
    xapitoken = json.loads(res.text)
    response = requests.post(f'https://gia.jd.com/jsTk.do?a={xapitoken["a"]}',cookies=cookies,headers=headers,data={'d':xapitoken["d"]})
    apitoken =  json.loads(response.text)
    data_param['x-api-eid-token'] = apitoken['data']['token']
    # print(apitoken['data']['eid'], end='   ')
    # response = requests.get('https://api.m.jd.com/', params=data_param, cookies=cookies, headers=headers)
    # cookies=cookies,
    response = base_spider(params=data_param,cookies=cookies,  headers=headers)
    return response
def paser_shopeabout(shopeabout):
    if shopeabout.replace(' ', '').replace('\t', ''):
        try:
            try:
                about = shopeabout.split('更多参数>>')[0].replace('___', '').replace('__', '_').replace('_', ',').replace(
                    '：', ':')
                if about[0] == ',':
                    about = about.replace(',', '', 1)
                about = '[' + ",".join(['"' + item.split(':')[0] + '"' + ':' + '"' + item.split(":")[1] + '"' for item in
                                        about.split(',')]) + ']'
            except:
                about = ''
            try:
                about_more = shopeabout.split('更多参数>>')[1].split('主体')[-1]
            except:
                about_more = ''



            about_more_list = []
            if about_more:
                body = about_more.replace('____', '').replace('__', '').replace('_', ',')
                if body[0] == ',':
                    body = body.replace(',', '', 1)
            else:
                body = ''

            # 主体 基本信息 存储 屏幕 电池信息 操作系统 网络支持  数据接口 摄像头  包装清单
            try:
                strb_1 = '"主体": ' + '"' + body.split('基本信息')[0] + '"'
            except:
                strb_1 = ''
            about_more_list.append(strb_1)
            try:
                strb_2 = '"基本信息": ' + '"' + body.split('基本信息')[1].split('存储')[0] + '"'
            except:
                strb_2 = ''
            about_more_list.append(strb_2)

            try:
                body = body.split('存储', 1)[1]
                strb_3 = '"存储": ' + '"' + body.split('屏幕', 1)[0] + '"'
            except:
                strb_3 = ''
            about_more_list.append(strb_3)
            try:
                strb_4 = '"屏幕": ' + '"' + body.split('屏幕', 1)[1].split('电池信息')[0] + '"'
            except:
                strb_4 = ''
            about_more_list.append(strb_4)

            try:
                body = body.split('电池信息', 1)[1]
                strb_5 = '"电池信息": ' + '"' + body.split('操作系统', 1)[0] + '"'
            except:
                strb_5 =' '

            about_more_list.append(strb_5)

            try:
                strb_6 = '"操作系统": ' + '"' + body.split('操作系统', 1)[1].split('网络支持')[0] + '"'
            except:
                strb_6 = ' '
            about_more_list.append(strb_6)
            try:
                body = body.split('网络支持', 1)[1]
                strb_7 = '"网络支持": ' + '"' + body.split('数据接口', 1)[0] + '"'
            except:
                strb_7 = ''
            about_more_list.append(strb_7)

            try:
                strb_8 = '"数据接口": ' + '"' + body.split('数据接口', 1)[1].split('摄像头', 1)[0] + '"'
            except:
                strb_8 = '"数据接口": '
            about_more_list.append(strb_8)
            try:
                body = body.split('摄像头', 1)[1]
                strb_9 = '"摄像头": ' + '"' + body.split('包装清单', 1)[0] + '"'
            except:
                strb_9 = '"摄像头": '
            about_more_list.append(strb_9)

            try:
                strb_10 = '"包装清单": ' + '"' + body.split('包装清单', 1)[1] + '"'
            except:
                strb_10 = '"包装清单": '
            about_more_list.append(strb_10)

            # print(about_more_list)
            return str(f'"商品介绍": {about}, "更多参数":{about_more_list}').replace(',', '，')
        except:
            return str(f'"商品介绍": {about}, "更多参数":{about_more_list}').replace(',', '，')

def parser(sku, js):
    # pprint.pprint(js)
    # 商品图片
    imageurl = 'https://img14.360buyimg.com/n1/' + js['wareInfo']['imageurl']

    # 店铺id
    shopid = js['wareInfo']['shopId']
    if shopid =='0':
        # 店铺名称
        shopname = '自营'
    else:
        # 店铺名称
        shopname = js['wareInfo']['wareInfoMap']['shop_name']
    try:
        # 商品配置
        shopetype = js['wareInfo']['wareInfoMap']['sale_attributes']
        shopetype= str([item['saleName']+' : '+ item['saleValue']  for item in json.loads(shopetype)])
    except:
        shopetype = ""
    if not shopetype:
        shopetype = " "
    # print(shopetype)
    name = js['wareInfo']['wname']
    price = js['price']['p']
    # /cookies=cookies,
    res = requests.get(f'https://item.jd.com/{sku}.html',cookies=cookies, headers=headers)
    res_text = res.text
    tree = etree.HTML(res_text)
    # 品牌树
    shopetitle = "".join(tree.xpath('//*[@id="crumb-wrap"]/div/div[1]//text()')).replace('\n','').replace('\r', '').replace('\t', '').replace(' ', '')
    # 品牌名
    shopename = shopetitle.split('>')[-1]
    # skuabout
    skuabout = re.findall('colorSize: (.*?\])',res_text)
    if skuabout:
        skuabout= str(skuabout[0])
    else:
        skuabout = " "



    # 商品配置
    shopeabout = "".join(tree.xpath('//*[@id="detail"]/div[2]//text()')).replace('\n', '_').replace('\r', '').replace('\t', '').replace(' ', '')
    shopeabout = paser_shopeabout(shopeabout)
    if shopeabout is None:
        shopeabout = " "

    # shopeabout = "".join(re.findall(r'([\u2E80-\u9FFF]+)', shopeabout))
    # print(shopeabout)
    # 判断是否存在促销
    # cx = ''
    # if len(js['promotion']['activity']) > 0:
    #     for item in js['promotion']['activity']:
    #         cx += item['text'] + ': ' + item['value'] + '\t'
    # cx = cx.replace('\n', '\t')
    # # 判断支持服务是否存在
    # sever_str = ''
    # list_server = js['servicesInfoUnited']['serviceInfo']['basic']['iconList']
    # if len(list_server) > 0:
    #     for item_server in list_server:
    #         sever_str += item_server['text'] + ' | '
    # sever_str = sever_str.replace('\n', '\t')
    print(sku, shopname, name,  price, end='\t')
    # print([sku, 'Apple', shopename, shopetitle, shopname, shopid, name, imageurl, shopetype, skuabout, shopeabout,  price])
    # 商品sku, 类别,商品品牌,类目树,店铺名,店铺id,                 商品标题,商品图片练链接,商品配置,sku配置,商品简介,价格,新增好评率
    return [sku, 'Apple', shopename, shopetitle, shopname, shopid, name, imageurl, shopetype, skuabout, shopeabout,  price]

def download(listdata, name="apple"):
    if not os.path.exists('apple.csv'):
        with open(f'{name}.csv', 'a', encoding='utf-8-sig') as f:
            f.write("商品sku, 类别,商品品牌,类目树,店铺名,店铺id,商品标题,商品图片练链接,商品配置,sku配置,商品简介,价格\n")
    with open(f'{name}.csv', 'a', encoding='utf-8-sig') as f:
        f.write(",".join(listdata)+'\n')

def main_func(sku, filename, cookies):
    jsdata = h5st_rquests(sku, cookies)
    list_data = parser(sku, jsdata)
    # 将逗号进行替换
    list_data = [item.replace(',', '，').replace('\r', '').replace('\n', '')+'\t' for item in list_data]
    download(list_data, filename)
    time.sleep(random.randint(7, 9))


if __name__ == '__main__':
    # 要获取的商品详情的 sku
    # item = "100066896214"
    # 保存的文件名
    filename = 'apple'
    # coookies 更换成自己的cookie
    cookies = {
        'shshshfpa': 'e91e0034-e13c-0944-39b4-01489f965443-1695450863',
        'shshshfpx': 'e91e0034-e13c-0944-39b4-01489f965443-1695450863',
        '__jdu': '1695561279547644995890',
        '_pst': 'jd_62af11cd38106',
        'unick': 'jd_62af11cd38106',
        'pin': 'jd_62af11cd38106',
        '_tp': '1j6Ksjx5rAflR60J%2B3VIzuWjsDODT3plDjQt8BDk0TY%3D',
        'areaId': '17',
        'ipLoc-djd': '17-1381-50712-62966',
        'autoOpenApp_downCloseDate_jd_homePage': '1696479418792_1',
        'user-key': '1b80f618-ddc7-4ed2-bbd9-d1f0d69384e1',
        'mt_xid': 'V2_52007VwMVWllcVVocTxFYAGEEF1dVUFZTF0gpWQBvUBJRDl1OXkxLS0AAMgpBTlUKUF8DSk0IAm5RRwJYW1QJL0oYXwd7AxNOXF9DWhdCGFoOZQYiUG1YYlIWSRpeAWQKE1VtXVVc',
        'warehistory': '"100058148818,100066896214,100066896214,100066896214,"',
        'autoOpenApp_downCloseDate_autoOpenApp_autoPromptly': '1696818601326_1',
        'jcap_dvzw_fp': 'OqkoLKIE86mhg_hnxYRJB2HTCrDDJ2iWrwWXlTJwfDir6XHXpNqmROgmhkO7omEY_VUsI3VU7WGyjbMhQE5fWQ==',
        'unpl': 'JF8EAMhnNSttCxlVAhoGHBtAGA4BW1RfTR5UbjUCXV1cTV1XHlUZExZ7XlVdXxRLFh9vZxRUVVNIUQ4aBSsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwaFE9aVF1bAE8SBWhiAFxVXEJcBCsDKxUge21UXVgBThAzblcEZB8MF1YDEgYSE11LWlxaWQ9LFAVnYwBSWl1OXA0fCxMTIEptVw',
        '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bc060568abbd48f78f0c681578c4f307|1697023446554',
        '3AB9D23F7A4B3CSS': 'jdd034TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBYAAAAMLE3VNGZQAAAAACQV5KWSUYRTBOUX',
        '_gia_d': '1',
        'PCSYCityID': 'CN_420000_420100_0',
        'joyya': '1697165011.0.22.0a1srmq',
        'shshshsID': '33911363276a76325e258a9adba18122_3_1697165011664',
        'jsavif': '1',
        '__jda': '122270672.1695561279547644995890.1695561280.1697092035.1697165004.25',
        '__jdc': '122270672',
        'mba_muid': '1695561279547644995890',
        'wlfstk_smdl': 'vd02rr4innhhtnytqke7bm6ed7wewzkr',
        'logintype': 'wx',
        'npin': 'jd_62af11cd38106',
        'thor': '04807F69E56567D32E6F641A647410B909F14B267E2BE31C03177EB0846D296ED6FE9D8A25B8FE78FE3438F255079F6E67A494C3162D57F7B039206DDBBEF1B4C73D0AFF8F5CF662CADA97DBB51F66B4D3CA0F1ABDE2694ACB1AF655AC496B5B81A8F1D8E0ABA58CD3F9763311651B62B1811C745EF29EC8CD2446B8F54B3F81121B6833E81A632C2B06F1E0F677A9EAC2BCC712FA875B94392071B1B69B63E1',
        'flash': '2_FAPMYE8_pYvYjkHcYlkOXOX3xjbS0Mxq1SDjRsZIgKsLJmqTvPWE7Eo1KlbMW6s10J7V8vVsDXPVqp5Ojzj2AZKxkmLUEv7i-DcsgQdMuSq*',
        'pinId': 'B_t2kVP0vYjKxe4Otrw_xrV9-x-f3wj7',
        '3AB9D23F7A4B3C9B': '4TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBY',
        'token': 'e7cceadd1a5768fef4fc8079dd548dac,3,942869',
        '__jdb': '122270672.8.1695561279547644995890|25.1697165004',
        'shshshfpb': 'AAj2i6yaLEh4ANOE8CUQ5tAFIn5ZUQxaVRQhjfwAAAAA',
    }
    headers = {
        'authority': 'api.m.jd.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'shshshfpa=e91e0034-e13c-0944-39b4-01489f965443-1695450863; shshshfpx=e91e0034-e13c-0944-39b4-01489f965443-1695450863; __jdu=1695561279547644995890; _pst=jd_62af11cd38106; unick=jd_62af11cd38106; pin=jd_62af11cd38106; _tp=1j6Ksjx5rAflR60J%2B3VIzuWjsDODT3plDjQt8BDk0TY%3D; PCSYCityID=CN_420000_420100_0; areaId=17; ipLoc-djd=17-1381-50712-62966; autoOpenApp_downCloseDate_jd_homePage=1696479418792_1; user-key=1b80f618-ddc7-4ed2-bbd9-d1f0d69384e1; mt_xid=V2_52007VwMVWllcVVocTxFYAGEEF1dVUFZTF0gpWQBvUBJRDl1OXkxLS0AAMgpBTlUKUF8DSk0IAm5RRwJYW1QJL0oYXwd7AxNOXF9DWhdCGFoOZQYiUG1YYlIWSRpeAWQKE1VtXVVc; unpl=JF8EAMdnNSttUEIEUBpXGxtHQwoHW1kKQx9WPW4NBw0NGAEMHQQSQhZ7XlVdXxRLFh9ubxRUXFNIVg4ZBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwaFE9aVF1bAE8SBWhiAFxVXEJcBCsDKxUge21SXVQBSRYzblcEZB8MF1wFEwIbXxBMVVBaWghIEQtrYgNTWF1DXAESChoiEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_98ad0d18f9fb45399dc89badbd8778a7|1696818214494; wlfstk_smdl=eztfxt59swq9eczhf4l96zk2tkkq4p8i; logintype=wx; npin=jd_62af11cd38106; thor=04807F69E56567D32E6F641A647410B909F14B267E2BE31C03177EB0846D296EAB5401AC71AD575ACD5D530E702307428AF0F818BF16C8F271162FFB0841D1221B3AB36CC4D2A4C831F332710AD130643D00EF791EB42287B625DBFABE78877BDFF626B1F4C7F48E42FB456AA57674431922407158BC24EA55DF3A16EFE06F1A40BDA581CBE6FEC895E2609F5D6CAAB08404D25A4E7C699B9A5602CF43097665; flash=2_6zA5nL-xT7qKBj79J9-TBK7WVhDpUCx9YLGvruC8SdrKOclDnVfZchKnkeJuZC0VzP_mmM8p66oR1XeNgDF5bqr7cH5vzLWyqrHjDd4zX5V*; pinId=B_t2kVP0vYjKxe4Otrw_xrV9-x-f3wj7; joyytokem=babel_3uUZrUyacoXXQpbzNmZdihzU2Z4RMDF2VGlUczk5MQ==.R2JQYktHbFxtRkZkWyo2MmcIPkNDOQdlDUd4X3hCWmUXZg1HKigVFBAHOxY4OhEBYDI4GyxsMCMFXCAyMB0HYSkjBRE1JSQFAT4VERUoFTI3Khc=.be0f6dbb; mba_muid=1695561279547644995890; warehistory="100058148818,100066896214,100066896214,100066896214,"; wxa_level=1; retina=1; cid=9; wqmnx1=MDEyNjM5OGkudTh0bFdUaSliMyxjbTBpMWZmNVlJRlI%3D; jxsid=16968186004626145374; webp=1; visitkey=20793055815849114; cd_eid=jdd034TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBYAAAAMLCJCQKKAAAAAADKLV4DSFVBW6B4X; equipmentId=4TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBY; fingerprint=edf3faab065a0968f2dec56a4abc449d; deviceVersion=117.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1696818601326_1; __wga=1696818601549.1696818601549.1696818601549.1696818601549.1.1; PPRD_P=UUID.1695561279547644995890-LOGID.1696818601561.427632425; sc_width=1626; jsavif=1; __jda=122270672.1695561279547644995890.1695561280.1696658247.1696818214.18; __jdc=122270672; token=742fc000306e08adeadb24205d9d9529,3,942677; __tk=addc3ff4fb88f7b01f25a50b92724711,3,942677; 3AB9D23F7A4B3C9B=4TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBY; mba_sid=16968186009356915316457673886.2; __jd_ref_cls=LoginDisposition_Feedback; joyya=1696818593.1696819243.49.1tk5kv0; 3AB9D23F7A4B3CSS=jdd034TGUABOZWY7C3HHN3BNBKXK3POLEATE4KJH2KYI4BEMGZWMW4F6DFHWPQXYBCR577YNJMC2OOS3ZOYZREJBCOC6NBYAAAAMLCJHUUSAAAAAADY7PQKOGCOAHMUX; _gia_d=1; shshshsID=15de5a4a9d6911021f818517f9d24e9d_5_1696819267198; __jdb=122270672.12.1695561279547644995890|18.1696818214; shshshfpb=AAoNLTxKLEh4ANOE8CUQ5tAFIn5ZUQxaVRQhjfwAAAAA',
        'origin': 'https://item.jd.com',
        'referer': 'https://item.jd.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-referer-page': 'https://item.jd.com/100066896214.html',
        'x-rp-client': 'h5_1.0.0',
    }

    # main_func(item, filename, cookies)
    with open('apple1.txt', 'r', encoding='utf-8-sig') as f:
        listdata = [item.replace('\n', '').replace(' ','') for item in f.readlines()]
    for item in listdata[1:]:
        item = item.replace(' ', '')
        main_func(item, filename, cookies)
        print(f"{item} is save over  count {listdata.index(item)}")


