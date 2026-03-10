import cv2
import numpy as np
# 使用opencv读取一张图片
image_input_rgb = cv2.imread('./wallpaper.jpg')
# image_input_rgb是一个矩阵
# print(type(image_input_rgb))

# 使用opencv接口进行灰度化将彩色图转化成灰度图
image_input_gray = cv2.cvtColor(image_input_rgb,cv2.COLOR_BGR2GRAY)
# 需要形状进行遍历
# image_shape = image_input_gray.shape
# print(image_shape)
#
# # 创建一个用来保存二值化的数组，形状跟灰度图一样
# image_input_twovalue = np.zeros(image_shape,dtype=np.uint8)


# 定义阈值法所需要的阈值
thresh = 127
# 定义阈值法所需要的最大值
max_val = 255

# # 二值化操作
# # 手写：
## # 需要将阈值和灰度值一一进行比较，因此遍历循环
# # 如果灰度值比阈值大，则设置成max_val,否则设置成0
# for i in range(image_shape[0]):
#     for j in range(image_shape[1]):
#         #如果灰度值比阈值大，则设置成max_val
#         if image_input_gray[i][j] > thresh:
#             image_input_twovalue[i][j] = max_val
#         # 否则设置成0
#         else:
#             image_input_twovalue[i][j] = 0
#
# # 显示结果
# cv2.imshow('image_input_rgb',image_input_rgb)
# cv2.imshow('image_input_gray',image_input_gray)
# cv2.imshow('image_input_twovalue',image_input_twovalue)

# 使用opencv调用接口对图像进行二值化灰度图
# 其中，ret存放的是阈值，image_thresh存放的是二值化图
ret,image_thresh = cv2.threshold(image_input_gray,thresh,max_val,cv2.THRESH_BINARY)
cv2.imshow('image_thresh',image_thresh)

cv2.waitKey(0)