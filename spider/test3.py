import cv2
import numpy as np

def find_template(template, image):
    # 获取模板的高度和宽度
    height, width, _ = template.shape

    # 提取模板的透明度通道
    mask = template[:, :, 3]
    mask_inv = cv2.bitwise_not(mask)

    # 提取模板的图像部分
    template_image = template[:, :, 0:3]

    # 将图像转换为三通道的 BGR 图像
    image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # 使用模板匹配方法
    result = cv2.matchTemplate(image_bgr, template_image, cv2.TM_CCOEFF_NORMED, mask=mask_inv)
    # 获取匹配位置
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    return max_loc

def main():
    # 读取大图片和小图片（包含透明度）
    big_image = cv2.imread('img/big.png', cv2.IMREAD_GRAYSCALE)
    small_image = cv2.imread('img/small.png', cv2.IMREAD_UNCHANGED)  # 读取包含透明度的图片

    # 在大图片中查找小图片位置
    match_loc = find_template(small_image, big_image)

    # 获取小图片的高度和宽度
    height, width, _ = small_image.shape

    # 在大图片中绘制匹配结果的矩形框
    top_left = match_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(big_image, top_left, bottom_right, (0, 255, 0), 2)

    # 保存绘制了匹配结果的图片
    cv2.imwrite('img/result_image.png', big_image)

if __name__ == "__main__":
    main()
