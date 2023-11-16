# -*- coding: utf-8 -*-
# @Time : 2023/4/19 11:34
# @Author : yogurt
import time
import openpyxl
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
# test
options = webdriver.ChromeOptions()
# 去除“Chrome正受到自动测试软件的控制”的显示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
# 设置headers
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
                       {"headers":
                            {
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                                }
                        })
# 防止网站检测selenium的webdriver
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => False
            })
        """})
# 窗口最大化
driver.maximize_window()


def get_save_data(tree,keywords):
    tb_list = tree.xpath('//*[@id="remark"]//dl')
    for item in tb_list:
        # 标题
        title = "".join(item.xpath('./dt/a//text()'))
        # 作者
        author = " ".join(item.xpath('./dd[3]/span[1]//a/@title'))
        # 来源
        source = " ".join(item.xpath('./dd[3]/span[2]/a/@title'))
        # 期刊
        date = " ".join(item.xpath('./dd[3]/span[3]//text()'))
        print(title, '\t', author, '\t', source, '\t', date)
        wb = openpyxl.load_workbook(f'./{keywords}.xlsx')
        ws = wb.active
        ws.append([title, author,source, date])
        wb.save(f'./{keywords}.xlsx')

def main(keywords):
    url = 'http://qikan.cqvip.com/Qikan/Search/Index?from=index'
    driver.get(url)
    time.sleep(2)
    element = driver.find_element(By.XPATH,'//*[@id="searchKeywords"]')
    element.send_keys(keywords)
    time.sleep(.5)
    element=  driver.find_element(By.XPATH,'//*[@id="btnSearch"]')
    element.click()
    tree = etree.HTML(driver.page_source)
    # 获取最大翻页数
    max_count = int(tree.xpath('//*[@id="headerpager"]/div/a[last()-1]//text()')[0])
    print("获取翻页数", max_count)

    for i in range(1, max_count):
        print("当前第", i, '页')
        # 数据存储
        get_save_data(tree, keywords)
        # 翻页
        element = driver.find_element(By.XPATH, '//*[@id="headerpager"]/div/a[3]')
        time.sleep(.5)
        element.click()
        # 睡眠避免速度太快导致触发反爬等机制
        time.sleep(3)

def creat_excle(name):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['标题', '作者', '来源', '期刊'])
    wb.save(f'./{name}.xlsx')

if __name__ == '__main__':
    keywords = "飞机"
    # 创建 excle
    creat_excle(keywords)
    main(keywords)
