import json

import requests


def getqG_json():
    return None
    url = "https://share.proxy.qg.net/get?key=8LYBGRUD&num=1&area=420100&isp=&format=json&seq=&distinct=true&pool=1"
    res = requests.get(url=url, timeout=5)
    js = json.loads(res.text)
    if js['code'] == 'SUCCESS':
        return {
            'http': 'http://' +  js['data'][0]['server'],
            'https': 'http://' +  js['data'][0]['server']
        }
    else:
        return None