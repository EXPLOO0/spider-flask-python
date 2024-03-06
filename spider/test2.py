import base64
import random
import time
import pyautogui

from DrissionPage._pages.web_page import WebPage
from DrissionPage._pages.chromium_page import ChromiumPage
import cv2



def is_existed(img_all='../spider/img/big.png', img='../spider/img/small.png', semilar=0.9):
    '''
    在img_all中寻找img，当相似度到达semilar时停止
    参数：
        img_all:
        img:
        semilar：相似度阀值
    返回：    (maxValue, maxLoc, Angle)
        maxValue: 相似度- 0：不相识，1：全相似
        maxLoc：最相似的位置（x，y）
        Angle：转换到最相似的旋转角度
    '''

    print('---3---')
    bg_img = cv2.imread(img_all)  # 背景图片
    tp_img = cv2.imread(img)  # 缺口图片
    print('---4---')

    if semilar <0 or semilar >1:
        semilar = 0.9

    max_val = 0  # 相似度
    # 取决于matchTemplate的最后一个参数，对于多数方法，越大越好；对于有2个方法，越小越好）
    angle = 0  # 旋转角度
    max_loc = (0,0)
    h, w = tp_img.shape[:2]

    for i in range(0, 360, 1):
        matRotate = cv2.getRotationMatrix2D((h*0.5, w*0.5), i, 1)
        dst = cv2.warpAffine(tp_img, matRotate, (h, w))
        # if i%30==0:
        #     show(dst)
        result = cv2.matchTemplate(
            bg_img, dst, cv2.TM_CCOEFF_NORMED)
        min_max_loc = cv2.minMaxLoc(result)  # 匹配程度最大的左上角位置 (x,y)
        if min_max_loc[1] > max_val:
            max_val = min_max_loc[1]
            max_loc =min_max_loc[3]
            angle = i
            # print(f'匹配度 = {max_val}, 旋转角度 = {i}')
            if max_val >= semilar:  # 很高的匹配度，认为已经ok了
                break
    # print(max_val)
    # print(max_loc)
    print(angle)
    # return (max_val, max_loc, angle)
    print(angle / 360 * 230)
    return angle / 360 * 230


def click_btn(page):
    if page.ele('.empty_button'):
        e_btn = page.ele('.empty_button')
        if e_btn:
            print('-----进行验证-------')
            e_btn.click()
            print('---.empty_button-1--')
            page.wait.load_start()
            print('---.empty_button-2--')
            if page.ele('#slider-div'):
                print('---.empty_button-3--')
                verify(page)
    elif page.ele('.verifyBtn'):
        e_btn = page.ele('.verifyBtn')
        if e_btn:
            print('-----进行验证-------')
            e_btn.click()
            print('---.verifyBtn-1--')
            page.wait.load_start()
            print('---.verifyBtn-2--')
            if page.ele('#slider-div'):
                print('---.verifyBtn-3--')
                verify(page)

def verify(page):
    i = 1
    while True:
        if page.ele('tag:div').attr('class') == 'container':
            print('--------验证界面---------')
            if page.ele('#img-back-div'):
                print('--------旋转界面---------')

                pass
            else:
                print('--------点击界面---------')
                return 1
            pass
        else:
            print('--------其他界面---------')
            return 1
        big_ele = page.ele('#img-back-div')
        small_ele = page.ele('#img-rotate-div')
        big_src = big_ele.attr('style')
        small_src = small_ele.ele('tag:img').link

        big_src = big_src[big_src.find(',') + 1:big_src.find('"); ')]
        small_src = small_src[small_src.find(',') + 1:]
        print(big_src)
        print(small_src)

        # 写入二进制文件
        with open('../spider/img/big-'+str(i)+'.png', mode='wb') as f:
            # 先转成二进制
            f.write(base64.b64decode(big_src))
        with open('../spider/img/small-'+str(i)+'.png', mode='wb') as f:
            # 先转成二进制
            f.write(base64.b64decode(small_src))

        i += 1

        page.ele('#slider-div').drag(10, 0, duration=0.1)

        # is_existed()
        #
        # res = is_existed()
        # print(res)
        # # res = res * 290 * 1.05 // 275
        # cl = page.ele('#slider-div')
        # lo = cl.rect.viewport_midpoint
        # x = int(lo[0] * 1.05) + 25
        # y = int(lo[1] * 1.05) + 90

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


if __name__ == '__main__':
    page = ChromiumPage()
    page.get('https://item.jd.com/10063504420346.html')
    click_btn(page)