import cv2
import numpy as np

# 获取彩色图
image_input = cv2.imread('./wallpaper.jpg')

# 灰度化
image_input_gray = cv2.cvtColor(image_input,cv2.COLOR_BGR2GRAY)

# 设置阈值和maxval
thresh = 127
maxval = 255

ret,image_input_thresh = cv2.threshold(image_input_gray,thresh,maxval,cv2.THRESH_BINARY_INV)

cv2.imshow('image_input_thresh',image_input_thresh)
cv2.waitKey(0)