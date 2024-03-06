from PIL import Image
import math


# def calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image):
#     pix_dict = {}
#
#     # 外圈长方形的宽高
#     outer_rectangle_width = outer_rectangle_image.width
#     outer_rectangle_height = outer_rectangle_image.height
#     print(outer_rectangle_width,outer_rectangle_height)
#     # 计算内圆图像的左上角坐标，将内圆放在外圈长方形的正中间
#     inner_circle_x = outer_rectangle_width  // 2
#     inner_circle_y = outer_rectangle_height // 2
#     print(inner_circle_x,inner_circle_y)
#
#     for angle in range(0, 360, 1):
#         # 内圆
#         x1 = outer_rectangle_width // 2 + inner_circle_radius * math.cos(angle * math.pi / 180)
#         y1 = outer_rectangle_height // 2 + inner_circle_radius * math.sin(angle * math.pi / 180)
#         point1 = inner_circle_image.load()[round(x1 - inner_circle_x), round(y1 - inner_circle_y)]
#         print(angle,x1,y1,point1)
#         # 外圈
#         # 计算长方形内部所有像素的颜色平均值
#         total_color = [0, 0, 0]
#         for i in range(outer_rectangle_width):
#             for j in range(outer_rectangle_height):
#                 pixel = outer_rectangle_image.load()[i, j]
#                 total_color[0] += pixel[0]
#                 total_color[1] += pixel[1]
#                 total_color[2] += pixel[2]
#
#         rectangle_color = [c // (outer_rectangle_width * outer_rectangle_height) for c in total_color]
#
#         # 求相似度
#         similarity = get_similarity(point1, rectangle_color)
#         pix_dict[angle] = similarity
#
#     return sorted(pix_dict.items(), key=lambda x: x[1])[0][0]
def calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image):
    pix_dict = {}

    # 内圆图像的尺寸
    inner_circle_width, inner_circle_height = inner_circle_image.size

    # 外圈长方形的宽高
    outer_rectangle_width = outer_rectangle_image.width
    outer_rectangle_height = outer_rectangle_image.height

    # 计算内圆图像的左上角坐标，将内圆放在外圈长方形的正中间
    inner_circle_x = inner_circle_width // 2
    inner_circle_y = inner_circle_height // 2

    # 获取内圆图像的像素数组
    inner_pixels = inner_circle_image.load()

    for angle in range(0, 361, 1):
        # 内圆
        x1 = outer_rectangle_width  // 2 + (inner_circle_radius) * math.cos(angle * math.pi / 180)
        y1 = outer_rectangle_height // 2 + (inner_circle_radius) * math.sin(angle * math.pi / 180)

        # 计算内圆上对应角度的像素
        inner_x = round(x1 - 95 )
        inner_y = round(y1 - 35 )

        # 外圈
        # 计算外圈上对应角度的像素
        # outer_x = round(x1+1)
        # outer_y = round(y1+1)
        outer_x = round(x1)
        outer_y = round(y1)

        # 获取内外圆上对应角度的像素颜色
        inner_color = inner_circle_image.load()[inner_x, inner_y]
        outer_color = outer_rectangle_image.load()[outer_x, outer_y]
        print(111,angle,inner_x,inner_y,inner_color)
        print(222,angle,outer_x,outer_y,outer_color)

        # 计算相似度
        similarity = get_similarity(inner_color, outer_color)
        pix_dict[angle] = similarity

    return sorted(pix_dict.items(), key=lambda x: x[1])[0][0]


def get_similarity(point1, point2):
    # 计算两个像素点之间的欧氏距离作为相似度
    squared_distance = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    similarity = math.sqrt(squared_distance)
    return similarity

def verifyRotate():
    # 示例用法
    inner_circle_radius = 50  # 内圆的半径
    outer_rectangle_image = Image.open("img/big.png")  # 外圈图像
    inner_circle_image = Image.open("img/small.png")  # 内圆图像

    similarity_angle = calculate_similarity(inner_circle_radius, outer_rectangle_image, inner_circle_image)
    print("Most similar angle:", similarity_angle)
    return similarity_angle

verifyRotate()