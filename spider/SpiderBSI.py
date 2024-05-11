import csv
import time

import pandas as pd
from DrissionPage._pages.chromium_page import ChromiumPage

from spider import SpiderVerify

def getBSI():
    page = ChromiumPage()

    # 初始化分类、型号文件
    with open("static/data/csv/data-brand.csv", mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['pid', 'p_brand1', 'p_brand2', 'p_brand3', 'p_brand4', 'p_brand5'])

    # 初始化图片文件
    with open("static/data/csv/data-spec-img.csv", mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['pid', 'p_img'])

    # 初始化介绍文件
    with open("static/data/csv/data-introduce.csv", mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['pid', 'param1', 'param2', 'param3'])

    # 初始化规格、包装文件
    with open("static/data/csv/data-spec.csv", mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['pid', 'param1', 'param2', 'param3', 'param4'])

    df = pd.read_csv('static/data/csv/data-goods.csv')
    # 只获取 pid 和 p_url
    df = df[['pid', 'p_url']]

    page.set.load_mode.eager()
    page.wait.load_start()
    for i in range(0, len(df)):

        print(df.at[i, 'p_url'])
        # 等待0.5s
        # time.sleep(0.5)

        page.get(df.at[i, 'p_url'])

        try:
            if page.ele('tag:div').attr('class') == 'container':
                print('------1.有验证------')
                SpiderVerify.click_btn(page)
                i -= 1
                continue
            elif page.ele('tag:input').attr('id') == 'pageSource':
                print('------1.登录------')
                SpiderVerify.login(page)
                i -= 1
                continue
            else:
                print('------1.无验证------')
                pass
        except:
            i -= 1
            continue

        # 分类、型号
        print('分类、型号---------------')
        try:
            j = 0
            while True:
                page.wait.ele_loaded(locator='.crumb fl clearfix', timeout=5, raise_err=False)
                brand_page = page.ele('.crumb fl clearfix')
                if not brand_page:
                    if page.ele('.container'):
                        print('------2.有验证------')
                        SpiderVerify.click_btn(page)
                    elif page.ele('tag:input').attr('id') == 'pageSource':
                        print('------2.登录------')
                        SpiderVerify.login(page)
                    else:
                        print('------2.无验证------')
                        pass
                    print('-----重新加载页面-------')
                    i -= 1
                    j = 1
                    break
                else:
                    break

            if j == 1:
                continue

            p_brand1 = brand_page.eles('.item first')[0].text
            p_brand2 = brand_page.eles('.item')[0].text
            p_brand3 = brand_page.eles('.item')[1].text
            p_brand4 = ' '
            if len(brand_page.eles('.item')) >= 3 :
                p_brand4 = brand_page.eles('.item')[2].text
            p_brand5 = brand_page.ele('.item ellipsis').text

            print(df.at[i, 'pid'], p_brand1, p_brand2, p_brand3, p_brand4, p_brand5)
            with open("static/data/csv/data-brand.csv", mode='a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow([df.at[i, 'pid'], p_brand1, p_brand2, p_brand3, p_brand4, p_brand5])
        except:
            i -= 1
            continue

        # 图片
        print('图片---------------')
        while True:
            try:
                page.wait.ele_loaded(locator='#spec-list', timeout=5, raise_err=False)

                if page.ele('#spec-list'):
                    imgList = page.ele('#spec-list').ele('tag:ul').eles('tag:li')
                else:
                    if page.ele('tag:div').attr('class') == 'container':
                        print('------1.有验证------')
                        SpiderVerify.click_btn(page)
                        i -= 1
                        continue
                    elif page.ele('tag:input').attr('id') == 'pageSource':
                        print('------1.登录------')
                        SpiderVerify.login(page)
                        i -= 1
                        continue
                    else:
                        print('------1.无验证------')
                        pass
                if len(imgList) != 0:
                    for imgLi in imgList:
                        if imgLi.ele('tag:img'):
                            img_src = imgLi.ele('tag:img').link or ' '
                            with open("static/data/csv/data-spec-img.csv", mode='a', newline='', encoding='utf-8') as f:
                                csv.writer(f).writerow([df.at[i, 'pid'], img_src])
                break
            except:
                continue

        # 介绍
        print('介绍---------------')
        if page.ele('tag:div').attr('class') == 'container':
            print('------1.有验证------')
            SpiderVerify.click_btn(page)
            i -= 1
            continue
        elif page.ele('tag:input').attr('id') == 'pageSource':
            print('------1.登录------')
            SpiderVerify.login(page)
            i -= 1
            continue
        else:
            print('------1.无验证------')
            pass
        page.wait.ele_loaded(locator='.p-parameter', timeout=5, raise_err=False)

        introduce_div = page.ele('.p-parameter')

        introduce_ul = introduce_div.eles('tag:ul')
        if introduce_ul[0].attr('id') == 'parameter-brand':
            brand = introduce_div.ele('#parameter-brand').text.split('：')
        else:
            brand = ['', '']

        with open("static/data/csv/data-introduce.csv", mode='a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([df.at[i, 'pid'], '1', brand[0], brand[1]])

        parameter_list = introduce_div.ele('.parameter2 p-parameter-list').eles('tag:li')

        for parameter in parameter_list:

            param = parameter.text.split('：')

            with open("static/data/csv/data-introduce.csv", mode='a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow([df.at[i, 'pid'], '2', param[0], param[1]])

        # 规格、包装
        print('规格、包装---------------')
        page.wait.ele_loaded(locator='.package-list', timeout=5, raise_err=False)

        t = page.ele('.package-list').ele('tag:h3').text

        s = page.ele('.package-list').ele('tag:p').text

        with open("static/data/csv/data-spec.csv", mode='a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([df.at[i, 'pid'], "包装", "包装", t, s])

        div = page.ele('#detail').ele('.tab-con').ele('.hide').ele('tag:div')
        if div.attr('class') == 'Ptable':
            try:
                if page.ele('.Ptable').eles('.Ptable-item'):
                    specList = page.ele('.Ptable').eles('.Ptable-item')

                    for spec in specList:

                        param2 = spec.ele('tag:h3').text

                        param3dlList = spec.ele('tag:dl').eles('.clearfix')
                        page.wait.ele_loaded(locator='.clearfix', timeout=5, raise_err=False)
                        for param3dl in param3dlList:

                            param3 = param3dl.ele('tag:dt').text

                            param4 = param3dl.ele('tag:dd').text

                            with open("static/data/csv/data-spec.csv", mode='a', newline='', encoding='utf-8') as f:
                                csv.writer(f).writerow([df.at[i, 'pid'], "规格", param2, param3, param4])
            except:
                i -= 1
                continue

        print('-----------第'+str(i)+'个-----------')
        if i % 500 == 0 and i != 0 :
            page.quit()
            page = ChromiumPage()
    page.quit()
