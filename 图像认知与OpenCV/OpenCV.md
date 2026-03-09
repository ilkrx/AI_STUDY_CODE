# OpenCV

## 1.计算机眼中的图像

```
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 生成三维数组
# 数据类型是整数
image = np.zeros((700,700,3),dtype=np.uint8)
# print(image)

# 用来代表分割出来的矩阵大小
block_size = 100

# 对黑色图像进行分割
# 方式一：
for i in range(0,700,block_size):

    #
    # 使用j来代表每一列
    for j in range(0,700,block_size):
        # i的取值：0， 100， 200， 300， 400， 500， 600
        # j的取值：0， 100， 200， 300， 400， 500， 600
        image[i,:,:] = (255,255,255)
        image[:,j,:] = (255,255,255)
        # 根据观察图像所得，i 和 j的取值都不能为0和600
        if i != 0 and j != 0 and i != 600 and j != 600 and (i == j or i + j == 600):
            # 在opencv中，颜色顺序是BGR
            image[i:i + block_size, j:j + block_size, :] = (0, 0, 255)

# 错误的切片形式
# image[0:700:100][0:700:100][:] = (255,255,255)
# image[0:700:100][:][:] = (255,255,255)
# image[:][0:700:100][:] = (255,255,255)

# 切片方式是下面这种形式
# 方式二：
# image[0:700:block_size, :, :] = (255, 255, 255)  # 所有水平线
# image[:, 0:700:block_size, :] = (255, 255, 255)  # 所有垂直线
# print(image[100:105])

# print(image[0:700:100][0:700:100][:])

# 将图像放在matplotlib的面板上画出来
# matplotlib的颜色顺序为RGB,需要进行BGR到RGB的转换
# 在image_rgb存饭的为RGB顺序的图像，在image里存放的是BGR顺序的图像
image_rgb =  cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.subplot(232)
# imshow是用来展示图像的
plt.imshow(image_rgb)
# title是用来给图像添加标签的
plt.title('Original Image')
# 不显示坐标轴
plt.axis('off')
# show函数，用来显示图像
# plt.show()


# 获取原图中的三个通道的像素值
# 有两种方法
# 第一种使用数组切片的方式去获取
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]

# 第二种：使用cv2.split()函数去分割
# b, g, r = cv2.split(image)

# 创建新的图像，用来展示三通道图
blue_channel = np.zeros((700, 700, 3), dtype=np.uint8)
green_channel = np.zeros((700, 700, 3), dtype=np.uint8)
red_channel = np.zeros((700, 700, 3), dtype=np.uint8)

# 将获取到的原图像的三通道的像素值，覆盖到新创建的三个图像的对应的通道
blue_channel[:, :, 0] = b
green_channel[:, :, 1] = g
red_channel[:, :, 2] = r

# 将BGR转换为RGB
blue_channel_rgb = cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB)
green_channel_rgb = cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB)
red_channel_rgb = cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB)

# plt.subplot() 用来对要展示的图像进行布局
# 131:创建1行3列的布局，并且本图像处于第1个位置
plt.subplot(234)
# 用来显示图像，但不能单独使用，需要配合plt.show()来显示
plt.imshow(blue_channel_rgb)
# 设置标签
plt.title("Blue Channel")
# 设置不显示坐标轴
plt.axis('off')

# 132:还是1行3列的布局，本图处于第2个位置
plt.subplot(235)
# 用来显示图像，但不能单独使用，需要配合plt.show()来显示
plt.imshow(green_channel_rgb)
# 设置标签
plt.title("Green Channel")
# 设置不显示坐标轴
plt.axis('off')

# 133:还是1行3列的布局，本图处于第3个位置
plt.subplot(236)
# 用来显示图像，但不能单独使用，需要配合plt.show()来显示
plt.imshow(red_channel_rgb)
# 设置标签
plt.title("Red Channel")
# 设置不显示坐标轴
plt.axis('off')

# plt.tight_layout()：作用就是合理布局图像
plt.tight_layout()

plt.show()


# cv2.imshow('image',image)
# cv2.waitKey(0)
```

## 2.灰度化

```
# import cv2
# import numpy as np
"""
# 使用opencv去读取一张图片，在opencv中使用cv2.imread取读取一张图片
# cv2.imread():两个参数，第一个是要读取的图片位置及名称（名称要包括文件的后缀名）
# 第二个参数是指定读取进来的图片格式，默认使用BGR彩色图的格式
image_np =  cv2.imread('./demo.png')
print(type(image_np))

# shape:是ndarray的一个属性，用来查看数组的形状
# shape读取到的形状与图像的实际宽和高是相反的，shape[0]图像的高度
# shape[1]图像的宽度
image_shape = image_np.shape

# 创建一个单通道的全零数组，此时就需要创建一个与原始图像大小相同的单通道数组
# image_gray就是我们创建的一个灰度图模板
image_gray = np.zeros((image_shape[0],image_shape[1]),dtype=np.uint8)

# 定义一个权重
weight_red = 0.299
weight_blue = 0.114
weight_green = 0.587


# 要遍历彩色图像，对彩色图像中的每个像素点都进行加权平均操作
# 从而求出每个像素点的灰度值，然后将得到的灰度值赋值给image_gray

# 通过一个嵌套循环让我们能够遍历图片中的所有像素点
# for i in range(image_shape[0]):
#     for j in range(image_shape[1]):
#         # 遍历到所有像素点之后，开始进行加权平均的计算
#         image_gray[i,j] = round(image_np[i,j][0]*weight_blue+image_np[i,j][1]*weight_green
#                            +image_np[i,j][2]*weight_red)

image_gray = (image_np[:, :, 0] * weight_blue +
              image_np[:, :, 1] * weight_green +
              image_np[:, :, 2] * weight_red).astype(np.uint8)


# 显示彩色图
cv2.imshow('image_np',image_np)
# 使用cv2.imshow（）去显示一下image_gray
cv2.imshow('image_gray',image_gray)
# 使用cv2.waitKey(0)将图像固定下来
cv2.waitKey(0)

"""


'''
        平均值方法
'''
"""
import cv2
import numpy as np

# 使用opencv去读取一张图片，在opencv中使用cv2.imread取读取一张图片
# cv2.imread():两个参数，第一个是要读取的图片位置及名称（名称要包括文件的后缀名）
# 第二个参数是指定读取进来的图片格式，默认使用BGR彩色图的格式
image_np =  cv2.imread('./demo.png')
print(type(image_np))

# shape:是ndarray的一个属性，用来查看数组的形状
# shape读取到的形状与图像的实际宽和高是相反的，shape[0]图像的高度
# shape[1]图像的宽度
image_shape = image_np.shape

# 创建一个单通道的全零数组，此时就需要创建一个与原始图像大小相同的单通道数组
# image_gray就是我们创建的一个灰度图模板
image_gray = np.zeros((image_shape[0],image_shape[1]),dtype=np.uint8)


# 要遍历彩色图像，对彩色图像中的每个像素点都进行加权平均操作
# 从而求出每个像素点的灰度值，然后将得到的灰度值赋值给image_gray

# 通过一个嵌套循环让我们能够遍历图片中的所有像素点
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 遍历到所有像素点之后，开始进行平均的计算
        t1 = (int(image_np[i,j][0])+int(image_np[i,j][1])+int(image_np[i,j][2]))//3
        image_gray[i, j] = t1


# 显示彩色图
cv2.imshow('image_np',image_np)
# 使用cv2.imshow（）去显示一下image_gray
cv2.imshow('image_gray',image_gray)
# 使用cv2.waitKey(0)将图像固定下来
cv2.waitKey(0)
"""

'''
       最大值方法  适用于原始图像比较暗的情况
'''
"""
import cv2
import numpy as np

# 使用opencv去读取一张图片，在opencv中使用cv2.imread取读取一张图片
# cv2.imread():两个参数，第一个是要读取的图片位置及名称（名称要包括文件的后缀名）
# 第二个参数是指定读取进来的图片格式，默认使用BGR彩色图的格式
image_np =  cv2.imread('./demo.png')
print(type(image_np))

# shape:是ndarray的一个属性，用来查看数组的形状
# shape读取到的形状与图像的实际宽和高是相反的，shape[0]图像的高度
# shape[1]图像的宽度
image_shape = image_np.shape

# 创建一个单通道的全零数组，此时就需要创建一个与原始图像大小相同的单通道数组
# image_gray就是我们创建的一个灰度图模板
image_gray = np.zeros((image_shape[0],image_shape[1]),dtype=np.uint8)


# 要遍历彩色图像，对彩色图像中的每个像素点都进行加权平均操作
# 从而求出每个像素点的灰度值，然后将得到的灰度值赋值给image_gray

# 通过一个嵌套循环让我们能够遍历图片中的所有像素点
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 遍历到所有像素点之后，并求最大
        t1 = np.max([image_np[i,j][0],image_np[i,j][1],image_np[i,j][2]])
        image_gray[i, j] = t1


# 显示彩色图
cv2.imshow('image_np',image_np)
# 使用cv2.imshow（）去显示一下image_gray
cv2.imshow('image_gray',image_gray)
# 使用cv2.waitKey(0)将图像固定下来
cv2.waitKey(0)
"""

'''
    opencv自带库去灰度化  opencv底层使用c++，比python要快
'''

import cv2
import numpy as np

# 使用opencv去读取一张图片，在opencv中使用cv2.imread取读取一张图片
# cv2.imread():两个参数，第一个是要读取的图片位置及名称（名称要包括文件的后缀名）
# 第二个参数是指定读取进来的图片格式，默认使用BGR彩色图的格式
image_np = cv2.imread('./demo.jpg')     # 注意：路径不能为中文
print(type(image_np))

#使用opencv接口去灰度化一张图像
cv_gray = cv2.cvtColor(image_np,cv2.COLOR_BGR2GRAY)

# 显示彩色图
cv2.imshow('image_np',image_np)
# 使用cv2.imshow（）去显示一下image_gray
cv2.imshow('image_gray',cv_gray)
# 使用cv2.waitKey(0)将图像固定下来
cv2.waitKey(0)
```

