import csv
import re
import time

from DrissionPage._pages.chromium_page import ChromiumPage

from spider import SpiderVerify


def getGoodsList(keyword, p):
    headers = {
        "Cookie": "shshshfpa=4ca191ff-53f0-8bae-8502-a1036427f352-1694775485; shshshfpx=4ca191ff-53f0-8bae-8502-a1036427f352-1694775485; __jdu=744904110; qrsc=3; _pst=jd_51f57c6a7950b; unick=jd_51f57c6a7950b; pin=jd_51f57c6a7950b; _tp=SQwJwPhztLc0Dk6FDRUju8WLLfk3W9eDpw2%2FvY165cc%3D; areaId=17; ipLoc-djd=17-1413-1416-56995; pinId=ZH5brpj5GCLkLjFIQPgRILV9-x-f3wj7; mt_xid=V2_52007VwUXV1VZV1ofSClaBTMHE1NeXk4JSE0cQAA1U0dODVoFXANBHV0EMlEUBV5RUVovShhfAHsCEU5cW0NaH0IZWg5nASJQbVhiWhxKHFoFYgoRU1toV1sWTw%3D%3D; TrackID=1YCFBt-oKew88aUWml0RTDyBEmEyUUyuDWUHiKXHVwIQuiHZYD71UoGi5IntIGZyKb90EET2b5q2ldfQwBjhpQJKnd7_WAHpb6ohvG1NhEeA; unpl=JF8EAK5nNSttD0lXAkwLGRoWTQpdWwgATR4Da2MMUF0LSgMHHgQTERJ7XlVdWBRKFB9uZBRXXFNJUg4YACsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrBB4XGEpYVF5cOEonBF9XNVdVXk5TASsDKxMgCQkIXlwASREAImEAUVVZTlQFGjIaIhM; user-key=698278b7-d600-4d80-a2a2-4450a0a41682; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_a379ae75074e49dcb7e1e989b6c66857|1707103042707; mba_muid=744904110; wlfstk_smdl=esnf8sowojh4eav4k6nyzcgrrnlpc7lr; thor=6465F1DAA2E71EAB7DDA2A69EBCA0834998A5F5832EE816E44E10F8193F7D99FFE82D2E3FE190AC99A77347D68BEAE0A424587C532D7C8AF7E836892D0BFF6D7F22B4CB0BE3219AE08A6712E451E0AF7832DA524B3BC201DA4D64A897452AEF42855C83D7E2695309BC5F58D2DB8502A8FEA44DCE3B373985602D73138EEF076A9169A96D235EFE23C8AEAE8EC042E655D78C0DA17811C331BBE996245E81E19; flash=2_P6jQrzlNGpqvDpCW9798UtxLwVbauOC7ujP0727amsdqtzb2hRr6c5TI6IBzdhvn3aeZAIn_o25bvJI6JFe4Uq_onSu9ju7QZYuvCMXeHuP*; ceshi3.com=000; jsavif=1; jsavif=1; rkv=1.0; avif=1; 3AB9D23F7A4B3C9B=XCLROUSW47ZSUYOPTPWJJDNPVO7YRZGZMHNLSMEMDV3UDLM3QV7X74W7O23TNXKGYCWRRVRHH3LF6BXDU6BCACCKBA; xapieid=jdd03XCLROUSW47ZSUYOPTPWJJDNPVO7YRZGZMHNLSMEMDV3UDLM3QV7X74W7O23TNXKGYCWRRVRHH3LF6BXDU6BCACCKBAAAAAMNO5EVF5AAAAAACAFKDSFKBEWB3IX; __jda=143920055.744904110.1694775482.1707101747.1707105581.31; __jdb=143920055.1.744904110|31.1707105581; __jdc=143920055; shshshsID=85915329fddb41f30d49b54a11ed2d6b_1_1707105581460; 3AB9D23F7A4B3CSS=jdd03XCLROUSW47ZSUYOPTPWJJDNPVO7YRZGZMHNLSMEMDV3UDLM3QV7X74W7O23TNXKGYCWRRVRHH3LF6BXDU6BCACCKBAAAAAMNO5V7HZAAAAAADLMA2XEV3WRYZIX; _gia_d=1; shshshfpb=BApXezWJjdOhAVz_vobdlGjfLyHTf4UKIB9Y2U6pX9xJ1MuvgoIO2"
        , 'Origin': 'https://search.jd.com',
        'Referer': 'https://search.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    url = 'https://search.jd.com/Search?keyword='
    url_page = p

    page = ChromiumPage()
    url = url + keyword

    page.get(url)
    with open("static/data/csv/data-goods.csv", mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(['pid', 'p_name', 'p_price', 'p_commit', 'p_shop', 'p_img', 'p_url'])

    for i in range(1, url_page + 1):
        if page.ele('.gl-warp clearfix'):
            print('------------')
        else:
            print('-----进行验证-------')
            SpiderVerify.click_btn(page)
            i -= 1
            continue
        page.scroll.to_top()
        time.sleep(1)
        page.scroll.to_bottom()
        time.sleep(1)
        page.scroll.to_bottom()
        time.sleep(1)
        ulele = page.ele('.gl-warp clearfix')
        if page.ele('.gl-warp clearfix'):
            print('------------')
        else:
            print('-----进行验证-------')
            SpiderVerify.click_btn(page)
            i -= 1
            continue
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