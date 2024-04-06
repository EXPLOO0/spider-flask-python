import cv2
from scipy import ndimage

def finPic(bg='img/big.png', tp='img/small.png', out='img/out.png'):
    '''
            bg: 背景图片
            tp: 缺口图片
            out:输出图片
            '''
    # 读取背景图片和缺口图片
    print('---3---')
    bg_img = cv2.imread(bg)  # 背景图片
    tp_img = cv2.imread(tp)  # 缺口图片
    #只取tp_img不透明的部分
    tp_img = tp_img[:,:,3]
    # 旋转图片tp 1度
    tp_img = ndimage.rotate(tp_img, 168)
    # 保存旋转后的图片
    cv2.imwrite('img/small_rotate.png', tp_img)

    print('---4---')

    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)

    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

    # for i in range(0, 360):

    # 旋转图片tp 1度
    tp_pic = ndimage.rotate(tp_pic, 168)
    # 保存
    cv2.imwrite('img/rotate.png', tp_pic)

    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

    # 绘制方框
    th, tw = tp_pic.shape[:2]
    tl = max_loc  # 左上角点的坐标
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    out = 'img/out-'+str(1)+'.png'
    cv2.imwrite(out, bg_img)  # 保存在本地


    x = (tl[0] + br[0]) / 2
    return x - 3


if __name__ == '__main__':
    finPic()