import base64
import random
import time
import pyautogui

import cv2

from PIL import Image
import math
import numpy as np
from DrissionPage.common import Actions

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
                return 1
                verifyRotate(page)
                pass
            else:
                print('--------点击界面---------')
                return 1
            pass
        else:
            print('--------其他界面---------')
            return 1

def verifyRotate(page):
    big_ele = page.ele('#img-back-div')
    small_ele = page.ele('#img-rotate-div')
    big_src = big_ele.attr('style')
    small_src = small_ele.ele('tag:img').link

    big_src = big_src[big_src.find(',') + 1:big_src.find('"); ')]
    small_src = small_src[small_src.find(',') + 1:]
    print(big_src)
    print(small_src)

    # 写入二进制文件
    with open('spider/img/big.png', mode='wb') as f:
        # 先转成二进制
        f.write(base64.b64decode(big_src))
    with open('spider/img/small.png', mode='wb') as f:
        # 先转成二进制
        f.write(base64.b64decode(small_src))
    res = rotate()
    print(res)
    res = res / 360 * 230


    print('res')
    print(res)

    # res = res * 290 * 1.05 // 275
    cl = page.ele('#slider-div')
    lo = cl.rect.viewport_midpoint
    x = int(lo[0] * 1.05) + 25
    y = int(lo[1] * 1.05) + 90

    # pyautogui.moveTo(x,y)
    # pyautogui.mouseDown(x,y)
    # pyautogui.moveTo(x + res + 15, y + 6, duration=0.5)
    # pyautogui.moveTo(x + res - 5, y -3, duration=0.6)
    # pyautogui.moveTo(x + res + 1, y , duration=0.4)
    # pyautogui.mouseUp()

    xx = x + res
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.mouseDown()
    y += random.randint(4, 15)
    # pyautogui.moveTo(xx + 10, y, duration=0.5)
    y += random.randint(-9, 0)
    pyautogui.moveTo(xx - 2, y, duration=random.randint(20, 31) / 100)
    y += random.randint(0, 8)
    pyautogui.moveTo(xx, y, duration=0.3)
    # pyautogui.sleep(0.5)
    pyautogui.mouseUp()

    time.sleep(3)

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

def calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image):
    print(2)
    pix_dict = {}

    # 获取内圆图像的尺寸
    inner_circle_width, inner_circle_height = inner_circle_image.size

    # 外圈长方形的宽高
    outer_rectangle_width = outer_rectangle_image.width
    outer_rectangle_height = outer_rectangle_image.height

    # 计算内圆图像的左上角坐标，将内圆放在外圈长方形的正中间
    inner_circle_x = outer_rectangle_width // 2
    inner_circle_y = outer_rectangle_height // 2

    # 获取内圆图像的像素数组
    inner_pixels = inner_circle_image.load()

    # 记录内圆周边像素颜色
    inner_circle_colors = []
    for angle in range(360):

        x = outer_rectangle_width  // 2 + (inner_circle_radius-3) * math.cos(angle * math.pi / 180) - 95
        y = outer_rectangle_height // 2 + (inner_circle_radius-3) * math.sin(angle * math.pi / 180) - 35
        # 取整
        x = round(x)
        y = round(y)

        # print(111,angle,x,y,inner_pixels[int(x), int(y)])
        inner_circle_colors.append(inner_pixels[int(x), int(y)])

    # 记录外圈接触区域的像素颜色
    outer_circle_colors = []
    for angle in range(360):
        x = outer_rectangle_width // 2 + (inner_circle_radius+3) * math.cos(angle * math.pi / 180)
        y = outer_rectangle_height // 2 + (inner_circle_radius+3) * math.sin(angle * math.pi / 180)
        # 取整
        x = round(x)
        y = round(y)
        outer_circle_colors.append(outer_rectangle_image.getpixel((int(x), int(y))))
        # print(222,angle,x,y,outer_rectangle_image.getpixel((int(x), int(y))))

    inner_colors_angle = []
    for angle in range(360):
        # 获取内圆在当前角度的全部边缘像素颜色
        # 将inner_circle_colors的所有数据后移一位，如1234变为4123
        inner_colors_angle.append(inner_circle_colors)
        inner_circle_colors_len = len(inner_circle_colors)-1
        inner_circle_colors = [inner_circle_colors[inner_circle_colors_len]]+ inner_circle_colors[0:inner_circle_colors_len]


        # 计算与外圈接触区域的相似度
        similarity = color_similarity(inner_colors_angle[angle], outer_circle_colors)
        # print(333,angle,similarity)
        pix_dict[angle] = similarity

    return sorted(pix_dict.items(), key=lambda x: x[1], reverse=True)[0][0]

def color_similarity(colors_rgba, colors_rgb):
    print(3)
    """
    计算两组颜色坐标中相同下标位置的像素颜色的相似度。

    :param colors_rgba: 包含RGBA四元组（带透明度）的列表
    :param colors_rgb: 包含RGB三元组（不带透明度）的列表
    :return: 相似度百分比（0到100之间）
    """
    num_pixels = len(colors_rgba)
    if num_pixels != len(colors_rgb):
        raise ValueError("两组颜色坐标的长度不一致")

    # 计算每个像素颜色之间的欧式距离，并计算平均距离
    total_distance = 0
    for i in range(num_pixels):
        rgba_color = colors_rgba[i][:3]  # 忽略透明度
        rgb_color = colors_rgb[i]
        distance = np.linalg.norm(np.array(rgba_color) - np.array(rgb_color))
        total_distance += distance

    # 计算相似度得分（距离越小，相似度越高）
    max_distance = 255 * np.sqrt(3)  # 最大距离对应于所有通道都是255
    similarity_score = 1.0 - (total_distance / (num_pixels * max_distance))
    similarity_percentage = similarity_score * 100

    return similarity_percentage


def rotate():
    print(1)
    # 示例用法
    inner_circle_radius = 50  # 内圆的半径
    outer_rectangle_image = Image.open("spider/img/big.png")  # 外圈图像
    inner_circle_image = Image.open("spider/img/small.png")  # 内圆图像

    similarity_angle = calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image)
    print("Most similar angle:", similarity_angle)
    return similarity_angle * 1.06

if __name__ == '__main__':
    rotate()