import cv2

image_input = cv2.imread('./wallpaper.jpg')


# 灰度化
image_gray = cv2.cvtColor(image_input,cv2.COLOR_BGR2GRAY)

# 使用opencv接口进行二值化操作
thresh = 127

maxval = 255

ret,image_thresh = cv2.threshold(image_gray,thresh,maxval,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(ret)

cv2.imshow('image_thresh',image_thresh)

cv2.waitKey(0)

# 使用cv2.imwrite()去保存图像
# 第一个参数是保存文件的路径以及图像全名包括后缀名
# 第二个参数是要保存的图像的数组
cv2.imwrite('thresh.png',image_thresh)