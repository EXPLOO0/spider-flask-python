import cv2
import numpy as np

# 加载大图片和小图片
big_image = cv2.imread('img/big.png', cv2.IMREAD_UNCHANGED)
small_image = cv2.imread('img/small.png', cv2.IMREAD_UNCHANGED)

# 提取大图片的圆形缺口区域
big_mask = np.zeros_like(big_image)
h, w = big_image.shape[:2]
cv2.circle(big_mask, (w // 2, h // 2), min(h, w) // 4, (255, 255, 255), thickness=-1, lineType=cv2.LINE_AA)

# 初始化最佳匹配度和对应的角度
best_match = 0
best_angle = 0

# 尝试不同的旋转角度，并找到最佳匹配度
for angle in range(0, 360):
    # 旋转小图片
    center = (small_image.shape[1] // 2, small_image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_small_image = cv2.warpAffine(small_image, rotation_matrix, (small_image.shape[1], small_image.shape[0]))

    # 将旋转后的小图片与大图片的圆形缺口区域进行叠加
    result = np.zeros_like(big_image)
    x_offset = (big_image.shape[1] - rotated_small_image.shape[1]) // 2
    y_offset = (big_image.shape[0] - rotated_small_image.shape[0]) // 2
    result[y_offset:y_offset + rotated_small_image.shape[0],
    x_offset:x_offset + rotated_small_image.shape[1]] = rotated_small_image

    # 计算重叠部分的像素和
    overlap = np.bitwise_and(result, big_mask)
    overlap_area = np.sum(overlap == 255)

    # 更新最佳匹配度和对应的角度
    if overlap_area > best_match:
        best_match = overlap_area
        best_angle = angle

# 输出最佳匹配度和对应的角度
print("Best match:", best_match)
print("Best angle:", best_angle)
