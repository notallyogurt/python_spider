# -*- coding:utf-8 -*-
import json
import os.path
import subprocess
import time
import requests

# 解决 pyinstaller 打包问题
class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        kwargs['encoding'] = "utf-8-sig"
        super().__init__(*args, **kwargs)
subprocess.Popen = MySubprocessPopen
os.environ["EXECJS_RUNTIME"] = "Node"

import execjs

with open('x-bogux.js', 'r', encoding='utf-8') as f:
    js = f.read()

def timestamp_to_date(timestamp):
    # 将时间戳转换为时间元组
    time_tuple = time.localtime(timestamp)
    # 格式化时间元组为年月日格式
    date = time.strftime("%Y-%m-%d", time_tuple)
    return date

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'ttwid=1%7CBtcabdi_9BMTbRjGckNG_pULdewK8uT7a3fKEUMneto%7C1696229777%7C0014d33f0cceb69e215e6782d641a6af675d4daa7c2e325f33bc97cf91cf832d; passport_csrf_token=fcdc2a25baec1dca7e68ac3e606acf1d; passport_csrf_token_default=fcdc2a25baec1dca7e68ac3e606acf1d; s_v_web_id=verify_ln8jf0ks_90IU6yEf_YZCY_4vFP_8njk_dRJOqAHI4I8K; xgplayer_user_id=405504239821; n_mh=VE6pqk3M5XMU1Go5EyQfkbovILqrxCWV-PBPRZFjEFU; _bd_ticket_crypt_doamin=3; _bd_ticket_crypt_cookie=d79115306386765671481140c4594c97; __security_server_data_status=1; store-region=cn-hb; store-region-src=uid; my_rd=2; LOGIN_STATUS=0; __live_version__=%221.1.1.4935%22; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1626%2C%5C%22screen_height%5C%22%3A1016%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221699840956.643%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSjJBTklJUFVoMlcweTlGY3BQM3JQbXlxWjlpZU1ObmFxNDhCakNnVjR0L05aTklpTGZGUEY3QXJyKzdvN2FNUFFWQjRLNzBzV1ZJWmlNVkZQSjllNkk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=ToTI37ceEQ5FGJdTSQPDQytzAsRGJOfkPL6XQVK0MEVxQuFgUYyKmuaf5A9hwognfd4d; download_guide=%221%2F20231113%2F0%22; pwa2=%220%7C0%7C1%7C0%22; __ac_nonce=0655183fb0091e112c1ac; __ac_signature=_02B4Z6wo00f01VnSDUgAAIDB2dD3CyCbUnVZ8gnAADMo8ekrocYoFZG3oiw0C4dkB8v95H9Ztpbb27x6wppBLqMxg7UV4BAeAxTXg8NHqYBYeMfqnJ4pL60IHpTzWiJ-QiZ1Waxld.VSACw220; SEARCH_RESULT_LIST_TYPE=%22single%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; msToken=09hD-x7gL4sn6QGY4c-QMyF7QAYyGY3MIqnU0ejvaZlua5gR0QO8yGs_k2YcvS_QweJJzFftG-vclfXpZa3qW8ADKQK1s8VFHHbZY0qXS-_BDY30ghUG8GHMjirgT_UZ; msToken=c407r5Snbc7G-zqJFy_uoU3CCbMlMYtJzHEktQKuzg5M1rvtxuEojN3MSxNqTAFB-3kPWYH2gmTYHEcJ4JfgF-yzNUm7UhYjFdgyQWBVJQ5DQ7v1aIgDt9cx8JzBKceR',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/search/python?aid=b439f888-6081-4277-993a-4dd60f33c3df&enter_from=discover&source=search_history',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def spider(keyword, sleeptime):
    errcount =0
    list_base = []
    offset = 1
    while len(list_base) < 200:
        # print("休眠", float(sleeptime))
        time.sleep(float(sleeptime))
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'search_channel': 'aweme_general',
            'sort_type': '0',
            'publish_time': '0',
            'keyword': keyword,
            'search_source': 'normal_search',
            'query_correct_type': '1',
            'is_filter_search': '0',
            'from_group_id': '',
            'offset': str(offset),
            'count': '10',
            'pc_client_type': '1',
            'version_code': '190600',
            'version_name': '19.6.0',
            'cookie_enabled': 'true',
            'screen_width': '1626',
            'screen_height': '1016',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '119.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '119.0.0.0',
            'os_name': 'Windows',
            'os_version':'10',
            'cpu_core_num': '20',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '50',
            'webid': '7285251353739314729',
            'msToken': '',
        }
        str_1 = ""
        for item in params.items():
            str_1 += item[0] + '=' + item[1] + '&'

        # context.execute(js)
        # X_Bogus = context.window.get_xbogux(str_1, None)
        X_Bogus = execjs.compile(js).call('window.get_xbogux', str_1, None)
        params['X-Bogus'] = X_Bogus
        print("生成的加密签名", X_Bogus)
        while True:
            try:
                response = requests.get('https://www.douyin.com/aweme/v1/web/general/search/single/', headers=headers, params=params, timeout=5)
                break
            except Exception as e:
                if errcount>3:
                    print(f"采集程序异常次数过多，本次采集即将结束，错误原因{e}, 请联系程序员进行定位错误原因")
                time.sleep(3)
                print(e)
                errcount += 1

        jsdata = json.loads(response.text)
        # print(jsdata)
        for item in jsdata['data']:
            if item.get('aweme_info'):
                try:
                    # 创建时间
                    createtime =timestamp_to_date(item['aweme_info']['create_time']) + '\t'

                    url = "https://www.iesdouyin.com/share/video/" + str(item['aweme_info']['aweme_id'])
                    # 标题
                    title = item['aweme_info']['desc'].replace('\n', ' ').replace('\r', '')
                    title_list = title.split('#', 1)
                    desc = ''
                    if len(title_list)>0:
                        desc = title_list[0]
                    if desc == '':
                        continue

                    # 话题
                    about = ''
                    if len(title_list)>1:
                        about = '# ' + title.split('#', 1)[1]
                    # 评论数
                    comment_count = str(item['aweme_info']['statistics']['comment_count'])
                    # 点赞数
                    digg_count = str(item['aweme_info']['statistics']['digg_count'])
                    # 下载量
                    download_count = str(item['aweme_info']['statistics']['download_count'])
                    # 转发量
                    share_count = str(item['aweme_info']['statistics']['share_count'])
                    print(len(list_base), desc,  createtime,  url)
                    list_base.append([url, desc,about, comment_count,digg_count, download_count, share_count, createtime])
                    if len(list_base) == 200:
                        return list_base

                except Exception as e:
                    # print(e)
                    pass
            else:
                pass
        offset += 10

    return list_base

def download(list_1, filename):
    if not os.path.exists(os.path.abspath('../../') + '\data'):
        os.mkdir(os.path.abspath('../../') + '\data')
    with open(f'../data/{filename}.csv', 'w', encoding='utf-8-sig') as f:
        f.write("链接, 标题, 话题, 评论数, 点赞数, 下载量, 转发量, 发布时间\n")
        for item in list_1:
            f.write(",".join(item)+'\n')

if __name__ == '__main__':
    # 进行强制睡眠让后续可以对此持续维护
    nowtime = int(time.time())
    slet = ((nowtime - 1699944477) // 86400 +1)*0.15
    slet = 0
    if os.path.exists('config.txt'):
        with open('config.txt', 'r', encoding='utf-8') as f:
            list_data = f.readlines()
    else:
        list_data = ['python']

    for filename in list_data:
        filename = filename.replace('\n', '').replace(' ', '').replace('\r', '')
        listbase = spider(filename, slet)
        download(listbase, filename)