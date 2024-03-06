import numpy as np

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

# 示例用法：
colors_rgba = [(178, 178, 178, 255), (178, 178, 178, 255), (169, 169, 169, 255)]  # 示例RGBA颜色
colors_rgb = [(254, 254, 254), (255, 255, 255), (253, 253, 253)]  # 示例RGB颜色
similarity = color_similarity(colors_rgba, colors_rgb)
print("相似度百分比:", similarity)

