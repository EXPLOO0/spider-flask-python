from PIL import Image
import math
import numpy as np

def calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image):
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

        x = outer_rectangle_width  // 2 + (inner_circle_radius-1) * math.cos(angle * math.pi / 180) - 95
        y = outer_rectangle_height // 2 + (inner_circle_radius-1) * math.sin(angle * math.pi / 180) - 35
        # 取整
        x = round(x)
        y = round(y)

        # print(111,angle,x,y,inner_pixels[int(x), int(y)])
        inner_circle_colors.append(inner_pixels[int(x), int(y)])

    # 记录外圈接触区域的像素颜色
    outer_circle_colors = []
    for angle in range(360):
        x = outer_rectangle_width // 2 + (inner_circle_radius) * math.cos(angle * math.pi / 180)
        y = outer_rectangle_height // 2 + (inner_circle_radius) * math.sin(angle * math.pi / 180)
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
        print(333,angle,similarity)
        pix_dict[angle] = similarity

    return sorted(pix_dict.items(), key=lambda x: x[1], reverse=True)[0][0]


def color_similarity(colors_rgba, colors_rgb):
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


def verifyRotate():
    # 示例用法
    inner_circle_radius = 50  # 内圆的半径
    outer_rectangle_image = Image.open("img/big.png")  # 外圈图像
    inner_circle_image = Image.open("img/small.png")  # 内圆图像

    similarity_angle = calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image)
    print("Most similar angle:", similarity_angle)
    return similarity_angle


verifyRotate()
