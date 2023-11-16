# -*- coding: utf-8 -*-
# @Time : 2023/4/26 15:35
# @Author : yogurt
import json
import re
import urllib.parse

import execjs
import requests
print(urllib.parse.quote('swisse'))
with open('tabao.js','r',encoding='utf-8') as f:
    jscode = f.read()



headers = {
    'authority': 'h5api.m.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_m_h5_tk=d35f1dd358b177d7c63f8f7108bf9dfd_1698232800326; _m_h5_tk_enc=daa45477a6ebd479614b449bc03ec530; cna=cra/HeKO+wYCATutHZgcf95S; xlly_s=1; t=cdf289977372e9ebdded241269d39e1c; _tb_token_=e3be7563e533e; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&existShop=false&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie14=Uoe9ZYSAyb6jJw%3D%3D&pas=0&cookie21=W5iHLLyFe3xm; csg=cbaea5c7; lgc=tb6382047342; cancelledSubSites=empty; dnk=tb6382047342; existShop=MTY5ODIyMzU2Ng%3D%3D; tracknick=tb6382047342; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=20c; _nk_=tb6382047342; x5sec=7b22617365727665723b32223a223966623331386162666466343537393138376238623334666632346338303935434c477a34366b47454c502b6a777361447a49794d4445304d7a51314e6a45784d6a41374e7967454d4f79586a4e4d4451414d3d222c22733b32223a2239393435643536653737623135333931227d; tfstk=dgeDHljPaSlXAgu0OZHf3yng-A1-GEMsGPptWA3Na4uWHfuOGPcgWzGaHxEYrVzLSceYBRVWIkZ_HiMOcxZjCA7d2pugcoMsnO_dpEqqhnkNJwBpw_Ym9APv7QsFUGfPuu9UFFGn-hwX6ShloWuU0qrYD8uyJ2rqrdJZrmXw3QRe4K9s4Gey1CGqV00KUcOxe; l=fBEi-FwnPEWYq9SkBOfZPurza77t_IRYmuPzaNbMi9fP9HfH5r8p7139c5YMCnGVF60DR3RpoAReBeYBqCcGSQLy2j-latDmnm9SIEf..; isg=BOjoQvjtGbMHozU3gnetxBOnudb6EUwbn0rZMqIZLWNQ_YhnSiPUqh839ZUNSQTz',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

# cook = {'isg': 'BE1Nm6kMFVwHvbFwgzOnJcQVXGnHKoH8eR3L-I_SieRThm04V3qRzJsU9BrgQpm0', 'l': 'fBQEPUVuNyIzRIxLBOfaFurza77OSIRYmuPzaNbMi9fPO85p5eY1W1ax9289C3GVFsipR3l39SNMBeYBqI4ZO_GJ2j-la_kmnmOk-Wf..', 'tfstk': 'chmRBx_31IAk_jd30uLcLsc_ozJcww5LTBVdv0Uooll8PS1D2cmOEMj3L5PJH', '_m_h5_tk_enc': '74c0b068dde4da5f7b0ad64dca0a10e0', '_m_h5_tk': '3ba546b50b48b8b21ff63650803cb8c0_1685102916276', '_l_g_': 'Ug%3D%3D', '_nk_': 'tb6382047342', 'existShop': 'MTY4NTA5MzU1NQ%3D%3D', 'cookie1': 'Vy%2BfUFkB4WLDF0HxI83DMu89HIgTm%2FBTgPenUpVov5M%3D', 'dnk': 'tb6382047342', 'cancelledSubSites': 'empty', 'sg': '20c', 'lgc': 'tb6382047342', 'csg': '2b474b27', 'uc3': 'nk2=F5RDL9UUDzskrem9&vt3=F8dCsfGbhoZEdLFwVKc%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UUphy%2FZ5ClMwHnGAdQ%3D%3D', 'unb': '2201434561120', 'skt': '37d6f4e680b42f0b', 'uc4': 'nk4=0%40FY4I7KrswUlTT4SFALTjbUeQ9RSA478%3D&id4=0%40U2grEJGGhMeyhIpggYP3TPxvNvGhjdOi', 'cookie2': '111504b5bf150a74b41c99f70b419032', 'sgcookie': 'E100jeo9VKlm82jib7lXyBpKWVOsUYDfHTkh3falKlPryUumk1%2B7Os%2BmO2HCWg8SaKJodB7Mhzsc%2BDSTqFoZGH3khgGFSMXDk3kXqKI1ENhOBnc%3D', 'uc1': 'existShop=false&cookie14=Uoe8j2f4FoNzTQ%3D%3D&pas=0&cookie21=Vq8l%2BKCLjA%2Bl&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D', '_cc_': 'W5iHLLyFfA%3D%3D', 'cookie17': 'UUphy%2FZ5ClMwHnGAdQ%3D%3D', 'JSESSIONID': 'DE8401D87E5C0C37A2668AFE1981ED42', 'xlly_s': '1', 'tracknick': 'tb6382047342', 'cna': 'sWr3HE1EM1QCAatxMXy+HB2w', 't': 'b65b4df1032815063ad0bda92b9074fc', '_tb_token_': 'ebab787537e8e', '_samesite_flag_': 'true'}

# cookie = 'cna=M3x0HA2AhSMCAWenhh3c24OL; tracknick=tb6382047342; _cc_=VFC%2FuZ9ajQ%3D%3D; thw=cn; lgc=tb6382047342; useNativeIM=false; mt=ci=-1_0; t=eeb6eb7465467902f5e249f1aec08d86; xlly_s=1; _m_h5_tk=8a92767226befcaac1184a25eeb769c0_1682498301257; _m_h5_tk_enc=d383d20cf51c3b39134b21db39e89a64; _tb_token_=f57fe634a3338; uc1=cookie14=Uoe8iCUiFxPFqw%3D%3D; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; tfstk=cbkCB_jPHwbCnA9lKytZCZCSiBw5ZyKbbT4KAeoTTLYlrziCidX4lEhbfN2z2l1..; l=fBObBlJnLVk1EYVQBOfZPurza77TbIRA_uPzaNbMi9fPOm1p5WMNW1NOab89CnGVF6RDR3kOuRA9BeYBqIccSQLy2j-la9Mmnm9SIEf..; isg=BOPj1fhqg4JvF0kkSJbx0zwncieN2Hca1MaD6RVAJMK5VAN2naqvaguGSiTac88S'
param_data = '{"id":"619614722913","detail_v":"3.3.2","exParams":"{\"ali_refid\":\"a3_430673_1006:1285280019:N:yrJoDxLc8bR9OdBKxFAN0Q==:bb8d1037586384f57d2188edf342ffc1\",\"ali_trackid\":\"1_bb8d1037586384f57d2188edf342ffc1\",\"id\":\"619614722913\",\"spm\":\"a2e0b.20350158.31919782.2\",\"queryParams\":\"ali_refid=a3_430673_1006%3A1285280019%3AN%3AyrJoDxLc8bR9OdBKxFAN0Q%3D%3D%3Abb8d1037586384f57d2188edf342ffc1&ali_trackid=1_bb8d1037586384f57d2188edf342ffc1&id=619614722913&spm=a2e0b.20350158.31919782.2\",\"domain\":\"https://detail.tmall.com\",\"path_name\":\"/item.htm\"}"}'
time_sign = execjs.compile(jscode).call('get_timeandsign', headers['cookie'], param_data)
print(time_sign)








# 评论
params = (
    ('jsv', '2.7.0'),
    ('appKey', '12574478'),
    ('t', f'{time_sign["time"]}'),
    ('sign', f'{time_sign["sign"]}'),
    ('api', 'mtop.alibaba.review.list.for.new.pc.detail'),
    ('v', '1.0'),
    ('type', 'json'),
    ('isSec', '0'),
    ('ecode', '0'),
    ('timeout', '10000'),
    ('dataType', 'json'),
    ('valueType', 'string'),
    ('ttid', '2022@taobao_litepc_9.17.0'),
    ('AntiFlood', 'true'),
    ('AntiCreep', 'true'),
    ('preventFallback', 'true'),
    ('type', 'json'),
    ('data', param_data),
)

# url = f"https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.2&appKey=12574478&t=1682494040862&sign=b3decf8f6ee4fa6513e0c719afb256eb&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data={data_1}"
response = requests.get(url= "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/",headers=headers,params=params)
print(response.text)




# list_all = re.findall('mtopjsonp3\((.*)\)',response.text)[0]
# print(list_all)
