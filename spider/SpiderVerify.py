import base64
import random
import time
import cv2
from DrissionPage.common import Actions
import configparser

def finPic(bg='spider/img/big.png', tp='spider/img/small.png', out='spider/img/out.png'):
    '''
            bg: 背景图片
            tp: 缺口图片
            out:输出图片
            '''
    # 读取背景图片和缺口图片
    print('---3---')
    bg_img = cv2.imread(bg)  # 背景图片
    tp_img = cv2.imread(tp)  # 缺口图片
    print('---4---')

    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)

    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

    # 绘制方框
    th, tw = tp_pic.shape[:2]
    tl = max_loc  # 左上角点的坐标
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    cv2.imwrite(out, bg_img)  # 保存在本地

    x = (tl[0] + br[0]) / 2
    return x - 3

def click_btn(page):
    print('-----点击按钮-------')
    page.wait.ele_loaded(locator = '.empty_button',timeout = 5,raise_err = False)
    page.wait.ele_loaded(locator = '.verifyBtn',timeout = 5,raise_err = False)
    if page.ele('.empty_button'):
        e_btn = page.ele('.empty_button')
        if e_btn:
            print('-----.empty_button-进行验证-------')
            e_btn.click()
            page.wait.load_start()
            if page.ele('.bg-blue') or page.ele('#slider-div'):
                verify(page)
    elif page.ele('.verifyBtn'):
        e_btn = page.ele('.verifyBtn')
        if e_btn:
            print('-----.verifyBtn-进行验证-------')
            e_btn.click()
            page.wait.load_start()
            if page.ele('.bg-blue') or page.ele('#slider-div'):
                verify(page)

def verify(page):
    while True:
        if page.ele('tag:div').attr('class') == 'container':
            print('--------验证界面---------')
            if page.ele('#cpc_img'):
                print('--------滑动界面---------')
                verifySlide(page)
                pass
            elif page.ele('#img-back-div'):
                print('--------旋转界面---------')
                time.sleep(1800)
                pass
            else:
                print('--------点击界面---------')
                return 1
            pass
        else:
            print('--------其他界面---------')
            return 1

def verifySlide(page):
    ac = Actions(page)

    big_ele = page.ele('#cpc_img')
    small_ele = page.ele('#small_img')
    big_src = big_ele.link
    small_src = small_ele.link

    big_src = big_src[big_src.find(',') + 1:]
    small_src = small_src[small_src.find(',') + 1:]
    print(big_src, small_src)

    # 写入二进制文件
    with open('spider/img/big.png', mode='wb') as f:
        # 先转成二进制
        f.write(base64.b64decode(big_src))
    with open('spider/img/small.png', mode='wb') as f:
        # 先转成二进制
        f.write(base64.b64decode(small_src))
    res = finPic() * 0.90
    print('res')
    print(res)
    # res = res * 290 * 1.05 // 275

    # cl = page.ele('.bg-blue')
    # lo = cl.rect.viewport_midpoint
    # x = int(lo[0] * 1.05) + 25
    # y = int(lo[1] * 1.05) + 90

    ac.move_to('.bg-blue')
    ac.hold()
    y = random.randint(-10, 10)
    ac.move(res-5, y, duration=0.1)
    y = random.randint(-5, 5)
    ac.move(6, y, duration=random.randint(20, 31) / 100)
    y = random.randint(-3, 3)
    ac.move(-3, y, duration=0.3)
    ac.release()

    # pyautogui.moveTo(x,y)
    # pyautogui.mouseDown(x,y)
    # pyautogui.moveTo(x + res + 15, y + 6, duration=0.5)
    # pyautogui.moveTo(x + res - 5, y -3, duration=0.6)
    # pyautogui.moveTo(x + res + 1, y , duration=0.4)
    # pyautogui.mouseUp()

    # xx = x + res
    # pyautogui.moveTo(x, y, duration=0.1)
    # pyautogui.mouseDown()
    # y += random.randint(4, 15)
    # # pyautogui.moveTo(xx + 10, y, duration=0.5)
    # y += random.randint(-9, 0)
    # pyautogui.moveTo(xx - 2, y, duration=random.randint(20, 31) / 100)
    # y += random.randint(0, 8)
    # pyautogui.moveTo(xx, y, duration=0.3)
    # # pyautogui.sleep(0.5)
    # pyautogui.mouseUp()

    time.sleep(1)

def verifyLoginSlide(page):
    ac = Actions(page)
    page.wait.ele_displayed('#JDJRV-suspend-warp JDJRV-bind-suspend-wrap ')
    while True:
        try:
            big_ele = page.ele('.JDJRV-bigimg').ele('tag:img')
            small_ele = page.ele('.JDJRV-smallimg').ele('tag:img')
        except:
            return 1

        if big_ele and small_ele:
            big_src = big_ele.link
            small_src = small_ele.link

            big_src = big_src[big_src.find(',') + 1:]
            small_src = small_src[small_src.find(',') + 1:]
            print(big_src, small_src)

            # 写入二进制文件
            with open('spider/img/big.png', mode='wb') as f:
                # 先转成二进制
                f.write(base64.b64decode(big_src))
            with open('spider/img/small.png', mode='wb') as f:
                # 先转成二进制
                f.write(base64.b64decode(small_src))
            res = finPic() * 0.59
            print('res')
            print(res)
            # res = res * 290 * 1.05 // 275

            ac.move_to('.JDJRV-slide-inner JDJRV-slide-btn')
            ac.hold()
            y = random.randint(-10, 10)
            ac.move(res - 5, y, duration=0.1)
            y = random.randint(-5, 5)
            ac.move(6, y, duration=random.randint(20, 31) / 100)
            y = random.randint(-3, 3)
            ac.move(-3, y, duration=0.3)
            ac.release()

            time.sleep(1)
        else:
            print('--------其他界面---------')
            return 1

def login(page):
    config = configparser.ConfigParser()
    config.read('configData.ini')  # 读取配置文件

    loginname = page.ele('#loginname')
    nloginpwd = page.ele('#nloginpwd')
    loginsubmit = page.ele('#loginsubmit')
    if loginname and nloginpwd and loginsubmit:
        name = config.get('User', 'name')
        pwd = config.get('User', 'pwd')

        loginname.input(name)
        nloginpwd.input(pwd)
        loginsubmit.check()

        # time.sleep(5)
        verifyLoginSlide(page)
    else:
        return 1
