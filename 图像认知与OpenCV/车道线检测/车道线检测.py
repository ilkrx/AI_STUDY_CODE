import cv2
import numpy as np

# 透视变换
def wrapper_image(image):
    # 获取原始图像的形状
    #                   高               宽
    origin_shape = [image.shape[0],image.shape[1]]
    # print(origin_shape)     #(270,480,3)
    # print(origin_shape)

    # 定义原始图像的四个点坐标
    # 顺序：上 右 下 左
    # 上左
    origin_up_left = [195,120]
    # 上右
    origin_up_right = [315,120]
    # 下右
    origin_down_right = [450,270]
    # 下左
    origin_down_left = [82,270]
    origin = np.float32([origin_up_left,origin_up_right,origin_down_right,origin_down_left])
    # 判断选取位置，看看是否合适
    # cv2.line(image,origin_up_left,origin_down_left,[0,0,255],1)
    # cv2.line(image,origin_up_right,origin_down_right,[0,0,255],1)

    # 定义透视变换之后的四个点坐标
    # 上左
    wrapper_up_left = [origin_shape[1] / 4,0]
    # 上右
    wrapper_up_right = [origin_shape[1] * 3 / 4,0]
    # 下右
    wrapper_down_right = [origin_shape[1] * 3 / 4,origin_shape[0]]
    # 下左
    wrapper_down_left = [origin_shape[1] / 4,origin_shape[0]]
    wrapper = np.float32([wrapper_up_left,wrapper_up_right,wrapper_down_right,wrapper_down_left])

    # 透视变换
    # 获取透视变换矩阵
    M = cv2.getPerspectiveTransform(origin,wrapper)

    # 进行透视变换
    image_wrapper = cv2.warpPerspective(image,M,(480,270))
    return image_wrapper

# 提取车道线
def extract_lines(image):
    # 去除图片中的噪声
    # 高斯滤波
    GaussianBlur_image = cv2.GaussianBlur(image,(3,3),3)
    # 转化为灰度图
    GaussianBlur_image_gray = cv2.cvtColor(GaussianBlur_image,cv2.COLOR_BGR2GRAY)
    # 转化为二值化图
    ret,GaussianBlur_image_binaryzation = cv2.threshold(GaussianBlur_image_gray,127,255,cv2.THRESH_BINARY)
    # 进行先膨胀后腐蚀操作:
    # 构建核
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,13))
    image_thresh = dilate_erode(GaussianBlur_image_binaryzation,kernel)

    # 基于梯度的方法
    image_sobel = cv2.Sobel(GaussianBlur_image_binaryzation,-1,1,0)
    return image_sobel

# 先膨胀后腐蚀
def dilate_erode(image_thresh,kernel):
    image_dilate = cv2.dilate(image_thresh,kernel)
    image_erode = cv2.erode(image_dilate,kernel)
    return image_erode


if __name__ == '__main__':
    for i in range(1, 8):
        # 读取图像
        image = cv2.imread(f'{i}.png')

        # 透视变换
        image_wrapper = wrapper_image(image)

        # 车道线提取
        image_sobel = extract_lines(image_wrapper)

        # 显示图像
        cv2.imshow(f'image_wrapper_{i}', image_wrapper)
        cv2.imshow(f'image_sobel_{i}', image_sobel)

        # 保存图像
        cv2.imwrite(f"final_{i}.png", image_sobel)

    # 等待按键后关闭所有窗口
    cv2.waitKey(0)