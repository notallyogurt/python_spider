import json
import os.path
import pprint
import time

import requests
import execjs

with open('tabao.js', 'r', encoding='utf-8') as f:
    jscode = f.read()


def dict_parser(text):
    if text:
        return str(text).replace(',', '，').replace('\r', '').replace('\n', '') + '\t'
    return ''


def token_params(param_data):
    time_sign = execjs.compile(jscode).call('get_timeandsign', headers['cookie'], param_data)
    params = (
        ('jsv', '2.7.2'),
        ('appKey', '12574478'),
        ('t', str(time_sign['time'])),
        ('sign', str(time_sign['sign'])),
        ('api', 'mtop.damai.mec.aristotle.get'),
        ('v', '3.0'),
        ('H5Request', 'true'),
        ('type', 'json'),
        ('timeout', '10000'),
        ('dataType', 'json'),
        ('valueType', 'string'),
        ('forceAntiCreep', 'true'),
        ('AntiCreep', 'true'),
        ('useH5', 'true'),
        ('data', param_data),
    )
    return params


headers = {
    'authority': 'mtop.damai.cn',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'cna=KXetHcyoqWsCATutHEm4Dmge; xlly_s=1; l=fBgV9QR7NW5virN_BO5CPurza779nIRb4sPzaNbMiIEGa6xf9FZ8KF5tqyr9WdtjgTCXTetyCykutdLHR3fRwxDDBEpsBwuK3xvtaQtJe; tfstk=d9tWfIwUX7V7AqTR8JM2G4NTZMII_QiZRJ6pIpEzpgIR9kOeL3RepXjBABR5J3JF26EBTp-yTpKFpHsk0UrFabjBpCSI_foZbg2OSMhZ_3MJELjA6V-mbcJkEMjK_foZESi4_GI_WcV02LygDoZNyj5HEloZbn6xt1pSik62cTgl1LCj6fBaXl56PjaQhNqCh1kjhy4nH4B54; isg=BFRUA1FCzSDuCVltxzRKF8FAJZLGrXiXufK8Qu414V-s2fYjFr7WIxsY3ffBIbDv; _m_h5_tk=55977eb9867ee5ea80cc2bdc573715f1_1697098076156; _m_h5_tk_enc=46e4eef04eb9f5fdeff1fae35868e8dd',
    'origin': 'https://m.damai.cn',
    'pragma': 'no-cache',
    'referer': 'https://m.damai.cn/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
}
list_title = ['标题', '明星', '开始时间', '所在城市', '举办地点', '价格区间', '最低门票', 'id', '售卖链接', '参与人数',
              '质量']

if not os.path.exists('save_info.csv'):
    with open("save_info.csv", 'w', encoding='utf-8-sig') as f:
        f.write(",".join(list_title) + '\n')


def spider_talk(id):
    data = '{"itemId":' + str(id).replace('\t',
                                          '') + ',"platform":"8","comboChannel":"2","dmChannel":"damai@damaih5_h5"}'
    params_talk = token_params(data)
    info_talkingnum = 0
    while True:
        try:
            res_tak = requests.get(
                'https://mtop.damai.cn/h5/mtop.alibaba.damai.detail.getdetail/1.2/',
                params=params_talk,
                headers=headers)
            js_child = json.loads(json.loads(res_tak.text)['data']['result'])

            # 预期
            number = dict_parser(
                js_child['detailViewComponentMap']['item']['dynamicExtData']['wantVO'].get(
                    'wantNumStr'))
            wantDesc = dict_parser(
                js_child['detailViewComponentMap']['item']['dynamicExtData']['wantVO'].get(
                    'wantDesc'))
            return [number, wantDesc]
        except:
            print("请求失误错误原因 进行重新请求 请等待")
            time.sleep(5)
            info_talkingnum += 1

            if info_talkingnum > 3:
                raise Exception(res_tak.text)
                exit()


city_list = ['852', '9999', '872', '906', '893', '1580', '1209', '200', '1377', '3250', '848', '2561', '1717', '253',
             '2161', '2053', '2348', '3264', '3126', '852', '1739', '2536', '1999', '2623', '2460', '2812', '776',
             '702', '3014', '1077', '727', '2392', '1377', '3140', '2628', '200', '2582', '1248', '1725', '2667',
             '2996', '1746', '1476', '1975', '1197', '917', '2017', '3178', '623', '923', '1826', '2593', '356', '553',
             '504', '893', '2103', '242', '9999', '2648', '1185', '2404', '3323', '1580', '2520', '949', '2007', '2483',
             '3167', '1819', '1637', '1116', '793', '2544', '667', '2574', '627', '956', '525', '2826', '1835', '1921',
             '2773', '1626', '1015', '962', '1653', '3037', '1755', '580', '653', '644', '482', '3379', '2189', '1229',
             '2902', '3368', '2337', '1314', '1691', '1175', '1561', '1989', '1781', '3387', '1962', '2037', '429',
             '1424', '2306', '2279', '2642', '968', '1403', '2762', '465', '1483', '1038', '2024', '415', '1103',
             '2265', '1397', '1597', '1790', '2295', '476', '1365', '379', '2200', '2785', '2329', '1847', '1028',
             '1277', '1667', '386', '1954', '1190', '929', '872', '3359', '565', '1643', '1703', '906', '2495', '600',
             '2840', '1169', '1087', '1450', '685', '1937', '2984', '1680', '1158', '2314', '1209', '3402', '2853',
             '2556', '1902', '1946', '1612', '586', '2528', '81', '1052', '65', '3250', '2', '372', '697', '3291',
             '770', '829', '4395', '659', '5105', '342', '2236', '3066', '3225', '2424', '2247', '1063', '1514', '3277',
             '1125', '1882', '999', '1137', '1413', '609', '172', '786', '54', '1765', '3335', '819', '3050', '1874',
             '937', '2374', '402', '977', '1148', '2148', '850', '848', '947', '1675', '913', '2207', '717', '1865',
             '1438', '276']

for city in city_list:
    city_save_start = 200
    for page in range(1, 100):
        #
        try:
            param_data = '{"args":"{\\"comboConfigRule\\":\\"true\\",\\"sortType\\":\\"10\\",\\"latitude\\":\\"0\\",\\"longitude\\":\\"0\\",\\"currentCityId\\":' + str(
                city) + ',\\"groupId\\":\\"2394\\",\\"pageIndex\\":' + str(
                page) + ',\\"pageSize\\":15,\\"comboCityId\\":\\"852\\",\\"platform\\":\\"8\\",\\"comboChannel\\":\\"2\\",\\"dmChannel\\":\\"damai@damaih5_h5\\"}","patternName":"category_solo","patternVersion":"4.0","dr":"[{\\"targetSectionId\\":\\"66c10b69-ad43-4aee-bd03-9a9bae3b5774\\",\\"targetLayerId\\":\\"0c5f1463-3e0b-43c5-ae8c-dd76e49264f3\\"}]","platform":"8","comboChannel":"2","dmChannel":"damai@damaih5_h5"}'
            params = token_params(param_data)
            if city_save_start == 200:
                response = requests.get('https://mtop.damai.cn/h5/mtop.damai.mec.aristotle.get/3.0/', headers=headers,
                                        params=params)
                jsdata = json.loads(response.text)
                list_savedata = []
                try:
                    jsdata = jsdata['data']['nodes'][0]['nodes'][0]['nodes']
                except:
                    raise Exception(jsdata['ret'])
                for item in jsdata:
                    sellhref = dict_parser(item['data'].get('schema'))
                    showTag = dict_parser(item['data'].get('showTag'))
                    showTime = dict_parser(item['data'].get('showTime'))
                    venueName = dict_parser(item['data'].get('venueName'))
                    priceStr = dict_parser(item['data'].get('priceStr'))
                    priceLow = dict_parser(item['data'].get('priceLow'))
                    cityName = dict_parser(item['data'].get('cityName'))
                    name = dict_parser(item['data'].get('name'))
                    id = dict_parser(item['data'].get('id'))
                    chilrdlist = [name, showTag, showTime, cityName, venueName, priceStr, priceLow, id, sellhref]
                    if chilrdlist.count('') == 8:
                        continue
                    elif chilrdlist.count('') == 9:
                        city_save_start = 404
                        break
                    else:
                        chilrdlist = chilrdlist + spider_talk(id)
                        list_savedata.append(chilrdlist)
                        time.sleep(.5)
                with open("save_info.csv", 'a', encoding='utf-8-sig') as f:
                    for item in list_savedata:
                        f.write(",".join(item) + '\n')
                print(f"城市id {city}, 所在页面{page} 已经存储完成")

            else:
                break
        except Exception as e:
            print(f"错误位置 {city}, 索引位置{city_list.index(city)}, 错误出现所在页面{page}", e)
            exit()
