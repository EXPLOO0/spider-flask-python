import csv
import re
import time

from DrissionPage._pages.chromium_page import ChromiumPage

from spider import SpiderVerify


def getGoodsList(keyword, p):
    url = 'https://search.jd.com/Search?keyword='
    url_page = p

    page = ChromiumPage()
    url = url + keyword

    # 获取页面
    page.get(url)
    # 给data-goods.csv写入标题行
    with open("static/data/csv/data-goods.csv", mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['pid', 'p_name', 'p_price', 'p_commit', 'p_shop', 'p_img', 'p_url'])
    #  循环获取页面
    for i in range(1, url_page + 1):
        # 判断是否为商品列表界面，为其他界面则进入自动登录或自动验证
        if page.ele('.gl-warp clearfix'):
            print('------------')
        elif page.ele('tag:input').attr('id') == 'pageSource':
            print('------1.登录------')
            SpiderVerify.login(page)
        else:
            print('-----进行验证-------')
            SpiderVerify.click_btn(page)
            i -= 1
            continue
        # 页面滚动到底部
        page.scroll.to_top()
        time.sleep(1)
        page.scroll.to_bottom()
        time.sleep(1)
        page.scroll.to_bottom()
        time.sleep(1)
        ulele = page.ele('.gl-warp clearfix')
        if page.ele('.gl-warp clearfix'):
            print('------------')
        elif page.ele('tag:input').attr('id') == 'pageSource':
            print('------1.登录------')
            SpiderVerify.login(page)
            i -= 1
            continue
        else:
            print('-----进行验证-------')
            SpiderVerify.click_btn(page)
            i -= 1
            continue
        #  获取商品信息
        liele = ulele.eles('.gl-item')
        for li in liele:
            div = li.ele('.gl-i-wrap')
            p_img = div.ele('.p-img').ele('tag:img').link or ' '
            p_price = div.ele('.p-price').ele('tag:strong').ele('tag:i').text or ' '
            p_name = div.ele('.p-name p-name-type-2').ele('tag:a').text.encode('GBK', 'ignore').decode('GBK', 'ignore') or ' '
            p_commit = div.ele('.p-commit').ele('tag:strong').ele('tag:a').text or 0
            p_shop = ''
            if li.ele('.p-shop'):
                if li.ele('.p-shop').ele('tag:span'):
                    if li.ele('.p-shop').ele('tag:span').ele('tag:a'):
                        p_shop = li.ele('.p-shop').ele('tag:span').ele('tag:a').text or ' '
            p_url = div.ele('.p-name p-name-type-2').ele('tag:a').link or ' '
            # 正则获取商品id
            err = 'pid'
            pattern = r"\d+"
            match = re.search(pattern, p_url)
            pid = ''
            if match:
                pid = match.group() or ' '
            print(pid, p_price, p_commit, p_shop, p_name, p_img, p_url)

            with open("static/data/csv/data-goods.csv", mode='a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow([pid, p_name,  p_price, p_commit, p_shop, p_img, p_url])
        #  翻页
        nextBTN = page.ele('.pn-next')
        zys = page.ele('.p-skip').ele('tag:em').ele('tag:b').text
        dqys = page.ele('.p-skip').ele('tag:input').value
        print('总页数：' + zys)
        print('当前页数：' + dqys)

        if int(zys) != int(dqys):
            nextBTN.click()
        else:
            break
    page.quit()