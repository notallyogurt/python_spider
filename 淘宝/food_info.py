# -*- coding: utf-8 -*-
# @Time : 2023/9/22 10:47
# @Author : yogurt
import json
import pprint
import urllib.parse
import execjs
import requests


with open('../../../Python_spider/2023Python/9/jd_tb/taobao/tabao.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
headers = {
    'authority': 'h5api.m.tmall.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'cookie2=139a7e238803717909bbec1bc888047d; t=526bb910e25b198c1e2e9d5d8a2606f6; _tb_token_=ea7733fe53514; xlly_s=1; x5sec=7b22617365727665723b32223a226233373863353965313134326137616632653538313939353534626434373761434d725538366b47454f616635622f2b2f2f2f2f2f77456f4244437a78664f462f502f2f2f2f384251414d3d222c22733b32223a2239343331616230633739393561373263227d; _m_h5_tk=611a7f6640beb6ae083e6a7ae8e12fdf_1698498517431; _m_h5_tk_enc=16e114813c4175bf96cb679424d2a454; _samesite_flag_=true; sgcookie=E1001qGDwQ4ylfhiu56PHvCucQ%2F8Z990QjYkR%2FK58s8kY8C2sRTTKlmy%2FVa7AwLIcEbiaaTaBeORCQkk15iRuVXHplK426XTy4tm0Tbi3nX1ooMm6xX0nO85ynRocu4Vs9fl; unb=2201434561120; uc3=id2=UUphy%2FZ5ClMwHnGAdQ%3D%3D&vt3=F8dD3CEHzm3ZBxSxBT4%3D&lg2=UtASsssmOIJ0bQ%3D%3D&nk2=F5RDL9UUDzskrem9; csg=8d56e04b; lgc=tb6382047342; cancelledSubSites=empty; cookie17=UUphy%2FZ5ClMwHnGAdQ%3D%3D; dnk=tb6382047342; skt=b0177a4c3c1d7313; existShop=MTY5ODQ5MTA2MA%3D%3D; uc4=nk4=0%40FY4I7KrswUlTT4SFALTjbFXLCsHVgUQ%3D&id4=0%40U2grEJGGhMeyhIpggYP3TP0J4mdYcpTl; tracknick=tb6382047342; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=20c; _nk_=tb6382047342; cookie1=Vy%2BfUFkB4WLDF0HxI83DMu89HIgTm%2FBTgPenUpVov5M%3D; mt=ci=8_1; thw=cn; cna=StjDHboYeBECATuulyMg7QD6; tfstk=dtMwvdqLfdpwdmU6w524L1Z7U9yT38LSsxabmmm0fP4gfqwqg4UChhe6M-u48qU_1R413xznqnB6XCF0uVegMfab5ryqD4-BPL9SXRKTZUTWF78wz88WAgsuKBnTH-Y5AtAWUc37xJ1GXg0PkZXQZMiu-AEBXFrhg7aFnTS8b5bIbs6V3LEgszV3GO7ckkfvRxhNosPgvkzWYHyXiZRf.; uc1=cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie14=Uoe9ZYIJvSzcwQ%3D%3D&cookie21=W5iHLLyFe3xm&pas=0; l=fBEi-FwnPEWYqSgAXOfaFurza77OSIRYYuPzaNbMi9fP_71B5KAkQ13pENY6C3GVFs_HR3RpoAReBeYBqQAonxvtNSVsr4DmndLHR35..; isg=BCwseUUAZcNpT3H75iOh0D_L_Qpe5dCPY7Yd_oZtOFd6kcybrvWgHyInsVkpGQjn',
    'pragma': 'no-cache',
    'referer': 'https://detail.tmall.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}
param_data = '{"pNum":2,"pSize":"60","refpid":"mm_26632360_8858797_29866178","variableMap":"{\\"q\\":\\"'+ str(("男鞋").encode("unicode_escape")) + '\\",\\"navigator\\":false,\\"clk1\\":\\"c6cfe44cbcd4e5a1aafbb48c6828e2aa\\",\\"union_lens\\":\\"recoveryid:201_33.50.160.167_79977828_1698490953112;prepvid:201_33.50.160.167_79977828_1698490953112\\",\\"recoveryId\\":\\"201_33.43.43.30_59961736_1698491191174\\"}","qieId":"36308","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.43.43.30_59961736_1698491191174","ctm":"spm-url:a2e0b.20350158.31919782.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632360_8858797_29866178%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3Dc6cfe44cbcd4e5a1aafbb48c6828e2aa%26upsId%3Dc6cfe44cbcd4e5a1aafbb48c6828e2aa%26spm%3Da2e0b.20350158.31919782.1%26pid%3Dmm_26632360_8858797_29866178%26union_lens%3Drecoveryid%253A201_33.50.160.167_79977828_1698490953112%253Bprepvid%253A201_33.50.160.167_79977828_1698490953112%26pnum%3D1"}'
time_sign = execjs.compile(jscode).call('get_timeandsign', headers['cookie'], param_data)
print(time_sign)


params = (
    ('jsv', '2.5.1'),
    ('appKey', '12574478'),
    ('t', f'{time_sign["time"]}'),
    ('sign', f'{time_sign["sign"]}'),
    ('api', 'mtop.alimama.union.xt.en.api.entry'),
    ('v', '1.0'),
    ('AntiCreep', 'true'),
    ('timeout', '20000'),
    ('AntiFlood', 'true'),

    ('data', param_data)
)


response = requests.get('https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/', headers=headers, params=params)
# print(response.text)
JSON = json.loads(response.text)
for item in JSON['data']['recommend']['resultList']:
    print(item)
    # exit()


# title = JSON['data']['item']['title']
# month_sell = JSON['data']['item']['vagueSellCount']
# buy_now = JSON['data']['pcTrade']['pcBuyParams']['buy_now']
# current_price = JSON['data']['pcTrade']['pcBuyParams']['current_price']
# region = JSON['data']['pcTrade']['pcBuyParams']['region']
# seller_nickname = JSON['data']['pcTrade']['pcBuyParams']['seller_nickname']
# buy_now, current_price, region, seller_nickname

# food_talk = JSON['data']['seller']['evaluates'][0]['score']
# sell_state = JSON['data']['seller']['evaluates'][1]['score']
# give_state = JSON['data']['seller']['evaluates'][2]['score']
# print(['商品名称', '月销', '现在购买', '当前售价', '发货地址', '店铺名称', '宝贝描述', '卖家服务', '物流服务'])
# # print(title, month_sell, food_talk, sell_state, give_state)
#
# #
# for canshu in JSON['data']['skuBase']['props']:
#     print(canshu)

# skus  种类
# for pageS in JSON['data']['skuBase']['skus']:
#     print(pageS['propPath'], pageS['skuId'])
#     for chilrd in pageS['propPath'].split(";"):
#         id = chilrd.split(":")[0]
#         id_c = chilrd.split(":")[1]
#         str_tip = ""
#         for canshu in JSON['data']['skuBase']['props']:
#             if canshu['pid'] == id:
#                 str_tip += canshu['name'] + ":"
#                 for canshu_child in canshu['values']:
#                     if canshu_child['vid'] == id_c:
#                         str_tip += canshu_child['name'] + " | "
#         print(str_tip)