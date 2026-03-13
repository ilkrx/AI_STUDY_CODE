# OpenCV

## 1.计算机眼中的图像

### 1.1 像素

​	像素是图像的基本单元，每个像素储存着图像的颜色、亮度和其他特征。一张图片是由很多个像素组成的。

### 1.2 RGB颜色

![1773147832775](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773147832775.png)

### 1.3 计算机中图像的存储

![1773147924085](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773147924085.png)

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

![1773147983392](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773147983392.png)

### 2.1 加权均值法

![1773148035874](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148035874.png)

### 2.2 平均值法

![1773148063661](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148063661.png)

### 2.3 最大值法

![1773148082371](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148082371.png)

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

## 3.二值化

​	==注意：此阈值是需要人工手动设置的！==

### 3.1 阈值法二值化

![1773148154290](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148154290.png)

```
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
```

### 3.2 反阈值法

![1773148175505](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148175505.png)

```
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
```

### 3.3 截断阈值法

![1773148185302](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148185302.png)

```
# 截断阈值法


import cv2
import numpy as np

# 首先还是使用opencv去读取一张图片
image_np = cv2.imread('./wallpaper.jpg')

# 2. 将读取到的彩色图进行灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 定义阈值法所需要的阈值
thresh = 150

# 定义阈值法所需要的最大值
maxval = 255

# 直接使用opencv的threshold函数去二值化
ret, image_thresh = cv2.threshold(image_gray, thresh, maxval, cv2.THRESH_TRUNC)

# # 为了能够遍历到灰度图的所有像素点，所以需要获取灰度图的形状
# image_shape = image_gray.shape
#
# # 创建一个与灰度图大小相同的单通道图像，用来接收灰度图与阈值比较的结果
# image_thresh = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)
#
# # 通过循环去遍历灰度图中的所有的像素点并和阈值进行比较
# for i in range(image_shape[0]):
#     for j in range(image_shape[1]):
#         # 让灰度图中的像素点的像素值与阈值进行比较
#         # 如果像素值超过阈值就设置为阈值
#         if image_gray[i, j] > thresh:
#             image_thresh[i, j] = thresh
#         # 否则的话，就不变
#         else:
#             image_thresh[i, j] = image_gray[i, j]

# 显示图像
# 显示灰度图与截断阈值法处理过的二值化图
cv2.imshow('image_gray', image_gray)
cv2.imshow('image_thresh', image_thresh)
cv2.waitKey(0)
```

### 3.4 低阈值0处理

​	像素值小于阈值部分设置成0，大于阈值的不变

![1773148204554](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148204554.png)

### 3.5 超阈值0处理

​	像素大于阈值部分设置成0，小于阈值的不变

![1773148214780](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148214780.png)

### 3.6 计算出合适的阈值

#### 3.6.1 使用opencv接口计算合适的阈值并进行二值化操作

```
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
```

#### 3.6.2 手写计算合适的阈值

![1773130576268](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773130576268.png)

![1773130588914](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773130588914.png)

```
import numpy as np
import cv2
# 读取彩色图
image_np = cv2.imread('./wallpaper.jpg')

# 使用cv2.resize去改变图像的宽和高
image_np = cv2.resize(image_np, (300, 300))

# 转换为灰度图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 使用np数组的min()函数去获取数组中的最小值
min_value = image_gray.min()

# 使用np数组的max()函数去获取数组中的最大值
max_value = image_gray.max()

# 使用np数组的shape属性获取灰度图的高度和宽度
image_shape = image_gray.shape

# 设置最大值
maxval = 255

# 生成一个二值化模板图
image_thresh = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)
# 定义计算最大类间方差公式中所用的变量
n_0 = 0
n_1 = 0
w_0 = 0
w_1 = 0
u_0 = 0
u_1 = 0
u = 0
rows = image_shape[0]
cols = image_shape[1]


# 定义一个字典，用来存储每一个阈值所对应的最大类间方差，方便后面获取合适的阈值
var = {}

# 用来控制阈值T取值的循环，其取值范围是灰度图中的(最小像素值+1, 最大像素值-1)
for t in range(min_value + 1, max_value, 1):
    # 定义一个列表用来存储前景像素点
    foreground = []

    # 定义一个列表用来存储后景像素点
    background = []

    # 定义一个变量用来存储前景的像素值的总数
    forepix = 0

    # 定义一个变量用来存储后景的像素值的总数
    backpix = 0

    # 定义一个变量用来求灰度图中所有的像素值的和
    pix = 0

    # 使用嵌套的for循环去遍历灰度图，用来区分在当前阈值下哪些点是前景点，哪些点是背景点
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            # 将灰度图的每个像素点去和阈值进行比较，如果大于阈值就是前景像素点
            if image_gray[i, j] > t:
                # 将前景像素点放到列表，方便后续去计算个数
                foreground.append([i, j])
                # 求前景像素点的总像素值
                forepix += image_gray[i, j]
                # 将该像素点的像素值加到pix里，用来统计图像的总像素值
                pix += image_gray[i, j]
            else:
                # 将后景像素点放到列表，方便后续去计算个数
                background.append([i, j])
                # 求后景像素点的总像素值
                backpix += image_gray[i, j]
                # 将该像素点的像素值加到pix里，用来统计图像的总像素值
                pix += image_gray[i, j]
    # 获取前景像素点数
    n_0 = len(foreground)
    # 获取背景像素点数
    n_1 = len(background)
    # 通过计算获取w0
    w_0 = n_0 / (image_shape[0] * image_shape[1])
    # 通过计算获取w1
    w_1 = n_1 / (image_shape[0] * image_shape[1])
    # 通过计算获取前景的平均像素值
    u_0 = forepix / n_0
    # 通过计算获取背景的平均像素值
    u_1 = backpix / n_1
    # 通过计算获取整幅图的平均像素值
    u = pix / (image_shape[0] * image_shape[1])

    # 通过最大类间方差公式去计算当前阈值下的最大类间方差的结果
    g = w_0 * ((u_0 - u) ** 2) + w_1 * ((u_1 - u) ** 2)

    # 将获取到的最大类间方差值和对于的阈值一块存储到字典中，方便后续选出最大值
    var[t] = g

# for循环结束后就可以去比较最大类间方差了
# 寻找字典中最大的值所对应的键
thresh = max(var, key=var.get)

# 使用一个嵌套循环去进行二值化操作
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 使用if判断灰度图中的第i行第j列的像素点的像素值与阈值的大小关系
        # 如果灰度图的第i行第j列比阈值大，就将该像素设置为maxval
        if image_gray[i, j] > thresh:
            image_thresh[i, j] = maxval
        # 否则的话，就设置为0
        else:
            image_thresh[i, j] = 0
print(thresh)
cv2.imshow('image_thresh', image_thresh)
cv2.waitKey(0)
```

## 4.自适应二值化

![1773148523988](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148523988.png)

![1773148553729](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148553729.png)

![1773148566450](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148566450.png)

### 4.1 取均值

![1773148869493](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773148869493.png)

### 4.2 加权求和

![1773149302444](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773149302444.png)

```
import cv2

# 读取彩色图片
image_input = cv2.imread('./wallpaper.jpg')

# 灰度化
image_gray = cv2.cvtColor(image_input,cv2.COLOR_BGR2GRAY)



# 自适应二值化
# cv2.adaptiveThreshold:是用来对单通道图进行自适应二值化的。
# 第一个参数：单通道图
# 第二个参数：二值化过程中所用到的最大值
# 第三个参数：计算阈值的方法： 1. 平均值法  cv2.ADAPTIVE_THRESH_MEAN_C  2. 使用高斯核的加权平均法 cv2.ADAPTIVE_THRESH_GAUSSIAN_C
# 第四个参数：二值化的方法：1. 阈值法 THRESH_BINARY， 2. 反阈值法 THRESH_BINARY_INV
# 第五个参数： blocksize ： 核的大小，通常为奇数  3*3， 5*5
# 第六个参数： 要减去的常数C的大小： 通常是正数，但也有可能是0或负数
image_thresh = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,10)

cv2.imshow('image_thresh',image_thresh)

cv2.waitKey(0)
```

## 5.形态学变换

![1773149634665](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773149634665.png)

![1773149980939](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773149980939.png)

### 5.1 腐蚀

```
# 对二值化图像进行腐蚀操作

# 先导入opencv的库，方便后续直接调用函数
import cv2

# 1. 读取一张要操作的彩色图像
image_np = cv2.imread('./img.png')

# 2. 将彩色图转化为灰度图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 将灰度图转化为腐蚀操作所需要的二值化图
ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# 4. 进行腐蚀操作：
# 4.1 构建腐蚀操作所需要用到的核
# cv2.getStructuringElement: 用来生成形态变换所需要用到的核
# 第一个参数：指定核的形状： cv2.MORPH_CROSS 表示十字形， cv2.MORPH_RECT 表示矩形  cv2.MORPH_ELLIPSE表示椭圆
# 第二个参数：指定核的大小： 以元组的形式传递
# 第三个参数：指定十字形核的核值分布
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))

# 4.2 去进行滑动计算
# erode: 用来对二值化图像进行腐蚀操作： 必须要准备两个参数
# 第一个：要进行腐蚀的二值化图像
# 第二个：用来滑动计算的结构化元素
image_erode = cv2.erode(image_thresh, kernel)

# 5. 显示图像
cv2.imshow('image_thresh', image_thresh)
cv2.imshow('image_erode', image_erode)
cv2.waitKey(0)
```

### 5.2 膨胀

```
# 对二值化图像进行膨胀操作


# 首先去导入opencv库，方便使用opencv的函数
import cv2

# 1. 读取图像
image_np = cv2.imread('./img.png')

# 2. 将彩色图像进行灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 将灰度图进行二值化
ret, image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# 4. 构建核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# 5. 膨胀操作
# dilate:用来对二值化图像进行膨胀操作
# 必须准备的两个参数：
# 第一个参数： 要膨胀的二值化图像
# 第二个参数： 构建好的结构化元素或者说核
image_dilate = cv2.dilate(image_thresh, kernel)

# 6. 显示图像
cv2.imshow('image_thresh', image_thresh)
cv2.imshow('image_dilate', image_dilate)
cv2.waitKey(0)
```

## 6.图像颜色识别

![1773199894846](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773199894846.png)

![1773199933872](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773199933872.png)

![1773210143819](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773210143819.png)

```
# 对图片中的某些目标颜色进行识别

# 导入opencv的库，方便后续直接调用函数
import cv2
import numpy as np

# 1. 图片输入：准备一张原始图片
image_np = cv2.imread('./color.png')

# resize: 将图像的大小进行修改，方便我们观察现象
image_np = cv2.resize(image_np, (700, 700))

# 2. HSV空间转换：将RGB颜色空间下的图像转化为HSV颜色空间下的图像
hsv_image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

# 3. 制作掩膜：为了方便后续遮挡其他不关心的区域，去制作一个掩膜

# 创建hsv颜色区域的最小值数组  针对黄色区域
lowerb = np.array([26, 43, 46])
# 创建hsv颜色区域的最大值数组  针对黄色区域
upperb = np.array([34, 255, 255])

# 使用inRange函数，将hsv图像中的每一个值与lowerb和upperb进行比较
# 当hsv图像中的像素点的hsv值处于数组范围之内，这个像素点就是我们要找的颜色

# inRange函数的作用：生成一个与原始图像大小相同的单通道图，其值要么是255，要么是0
# 第一个参数：原始图像
# 第二个参数：寻找的范围的最小值  是个数组
# 第三个参数：寻找的范围的最大值  是个数组
mask_image_np = cv2.inRange(hsv_image_np, lowerb, upperb)

# 4. 与运算：将原始图像和原始图像进行位与操作，并使用掩膜去遮盖掉不关心的部分
color_image_np = cv2.bitwise_and(image_np, image_np, mask=mask_image_np)

# 5. 图像输出：把结果显示出来
cv2.imshow("mask_image_np", mask_image_np)
cv2.imshow('color_image_np', color_image_np)
cv2.waitKey(0)
```

## 7.图像颜色替换

​	在颜色识别的基础上进行开操作，然后在开操作之后的掩膜中找到要替换的坐标位置，将位置上的值修改为替换的颜色的值。

```
# 导入OpenCV库，方便调用函数
import cv2
import numpy as np

# 1. 图片输入，将图片读取进来
image_np = cv2.imread('./color.png')
cv2.imshow('image_np', image_np)

# 2. 将图片转换为HSV模型下的图片
image_hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

# 3. 制作掩膜
color_lower = np.array([0, 43, 46])
color_high = np.array([10, 255, 255])
image_mask = cv2.inRange(image_hsv, color_lower, color_high)

# 4. 开运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
image_mask_open = cv2.morphologyEx(image_mask, cv2.MORPH_OPEN, kernel)

# 5. 图片颜色替换
# for i in range(image_mask_open.shape[0]):
#     for j in range(image_mask_open.shape[1]):
#         if image_mask_open[i, j] == 255:
#             image_np[i, j] = (255, 0, 0)
image_np[image_mask_open == 255] = (255, 0, 0)

# 6. 显示结果
cv2.imshow('image_np1', image_np)
cv2.imshow('image_mask_open', image_mask_open)
cv2.waitKey(0)
```

## 8.ROI切割

![1773236346783](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773236346783.png)

```
# 这个文件的作用是用来对图像中的某些区域进行切割的

# 导入opencv库，方便读取和显示图像
import cv2

# 1. 读取我们要切割的图像
image_np = cv2.imread('./lena.png')

# 获取图像的高度和宽度，方便后续进行判断
height, width = image_np.shape[0], image_np.shape[1]

try:
    # 2. 切割感兴趣的区域
    # 人为指定我们要切割的区域
    x_min, x_max = 270, 400
    y_min, y_max = 270, 400

    # 对要切割的区域的范围进行判断
    if not (x_min >= 0 and x_max <= width and y_min >= 0 and y_max <= height):
        raise OverflowError("x_min or x_max or y_min or y_max overflow!!")

    # 使用cv2.rectangle去画一个矩形框，方便我们去调整感兴趣的区域的范围
    cv2.rectangle(image_np, (x_min - 2, y_min - 2), (x_max + 2, y_max + 2), (0, 0, 255), 2)

    # 3. 使用np数组的切片操作对图像进行切割
    image_roi = image_np[y_min: y_max, x_min: x_max]
    # 4. 显示结果
    cv2.imshow('image_np', image_np)
    cv2.imshow('image_roi', image_roi)
    cv2.waitKey(0)
except Exception as e:
    print(e)
```

## 9.图像旋转

![1773279429130](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773279429130.png)

### 9.1 单点旋转

![1773279963176](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773279963176.png)

![1773302907763](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773302907763.png)

### 9.2 插值方法

![1773313420178](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313420178.png)

#### 9.2.1 最近邻插值

![1773313488770](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313488770.png)

![1773313527966](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313527966.png)

#### 9.2.2 双线性插值

![1773313611372](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313611372.png)

![1773313642622](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313642622.png)

![1773313666726](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313666726.png)

![1773313687924](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313687924.png)

### 9.3 边缘填充

![1773313788846](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313788846.png)

#### 9.3.1 边界复制

![1773313826110](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313826110.png)

#### 9.3.2 边界反射

![1773313852045](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313852045.png)

#### 9.3.3 边界反射101

![1773313881812](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313881812.png)

#### 9.3.4 边界常数

![1773313901616](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313901616.png)

#### 9.3.5 边界包裹

![1773313922270](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773313922270.png)

## 10.图像镜像旋转

![1773314370159](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773314370159.png)

```
# 对图像进行翻转操作
import cv2

# 导入OpenCV的库，方便我们调用函数

# 1. 读取图片
image_np = cv2.imread('./lena.png')

# 2. 使用flip函数去对图像进行镜像的翻转
# cv2.flip： 对图像进行镜像翻转
# 第一个参数：要翻转的原始图像
# 第二个参数：标志位， 0：表示绕x轴进行上下翻转， >0:表示绕y轴进行左右翻转  <0:表示绕x轴和y轴各进行一次翻转
image_flip = cv2.flip(image_np, 0)

# 3. 输出，显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_flip', image_flip)
cv2.waitKey(0)
```

## 11.图像缩放

```
# 导入OpenCV的库
import cv2

# 1.图片输入，读取一张图片
image_np = cv2.imread('./lena.png')

# 2. 图片缩放
# dsize和fx、fy不能同时使用，如果同时出现，会以dsize的标准进行缩放
# 如果想要使用resize函数，就必须填入两个参数：src和dsize
# 如果不想使用dsize，赋为None就行。
image_resize = cv2.resize(image_np, dsize=None, fx=0.1, fy=1, interpolation=cv2.INTER_LINEAR)

# 3. 显示图像
cv2.imshow('image_np', image_np)
cv2.imshow('image_resize', image_resize)
cv2.waitKey(0)
```

## 12.图像矫正

![1773318377852](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773318377852.png)

![1773318390165](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773318390165.png)

```
# 导入OpenCV库，方便调用函数
import cv2
import numpy as np

# 1. 读取图片
image_np = cv2.imread('./test.png')

# 获取图像的大小
img_shape = image_np.shape

# 2. 定义原始图像中的四个顶点的坐标
points1 = np.float32([[200, 100], [700, 150], [140, 400], [650, 460]],)
# 定义目标图像中 这四个顶点坐标所对应的位置
points2 = np.float32([[0, 0], [img_shape[1], 0], [0, img_shape[0]], [img_shape[1], img_shape[0]]])

cv2.line(image_np, points1[0].astype(np.int64).tolist(), points1[1].astype(np.int64).tolist(), (0, 0, 255), 1,lineType=cv2.LINE_8)
cv2.line(image_np, points1[0].astype(np.int64).tolist(), points1[2].astype(np.int64).tolist(), (0, 0, 255), 1,lineType=cv2.LINE_8)
cv2.line(image_np, points1[3].astype(np.int64).tolist(), points1[1].astype(np.int64).tolist(), (0, 0, 255), 1,lineType=cv2.LINE_8)
cv2.line(image_np, points1[3].astype(np.int64).tolist(), points1[2].astype(np.int64).tolist(), (0, 0, 255), 1,lineType=cv2.LINE_8)

# 3. 获取透视变换矩阵
M = cv2.getPerspectiveTransform(points1, points2)

# 4. 进行透视变换
image_warpPerspective = cv2.warpPerspective(image_np, M, (img_shape[1], img_shape[0]), flags=cv2.INTER_CUBIC)

# 5. 显示图像
cv2.imshow('image_np', image_np)
cv2.imshow('image_warpPerspective', image_warpPerspective)
cv2.waitKey(0)
```

## 13.图像添加水印

![1773319660567](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773319660567.png)

```
# 导入OpenCV的库
import cv2
 
 
# 1. 读取原始图像和模板图
image_np = cv2.imread('./lena.png')
logo = cv2.imread('./logo.png')
cv2.imshow('image_np', image_np)
# 获取logo图的大小
rows, cols = logo.shape[:2]
 
 
# 截取原始图像的ROI区域
roi = image_np[100:100+rows, 100:100+cols]
cv2.imshow('roi', roi)
# 2. 对logo进行灰度化和二值化，制作成一张掩膜
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
 
ret, mask = cv2.threshold(logo_gray, 127, 255, cv2.THRESH_BINARY_INV)
 
# 3. 进行与运算
image_and = cv2.bitwise_and(roi, roi, mask=mask)
 
# 4. 图像融合
dst = cv2.add(image_and, logo)
 
# 5. 将融合后的图像重新赋值到原始图像中
image_np[100:100+rows, 100:100+cols] = dst
 
 
# 6. 显示结果
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.imshow('image_and', image_and)
cv2.imshow('image_np1', image_np)
cv2.waitKey(0)
```

## 14.图像噪点消除

![1773368410301](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773368410301.png)

### 14.1 均值滤波

![1773368480674](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773368480674.png)

```
# 导入OpenCV的库
import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 获取卷积核（滤波器）并进行均值滤波操作
image_blur = cv2.blur(image_np, (5, 5))

# 3. 显示结果
cv2.imshow('image_np', image_np)
cv2.imshow('image_blur', image_blur)
cv2.waitKey(0)
```

### 14.2 方框滤波

![1773368534877](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773368534877.png)

![1773368549001](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773368549001.png)

```
# 导入OpenCV的库
import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接进行方框滤波
image_box = cv2.boxFilter(image_np, -1, (3, 3), normalize=False)

# 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_box', image_box)
cv2.waitKey(0)
```

### 14.3 高斯滤波

![1773369564596](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369564596.png)

![1773369584767](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369584767.png)

```
# 导入OpenCV的库
import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接进行高斯滤波
image_Gaussian = cv2.GaussianBlur(image_np, (5, 5), 3)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Gaussian', image_Gaussian)
cv2.waitKey(0)
```

### 14.4 中值滤波

![1773369635257](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369635257.png)

![1773369647804](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369647804.png)

![1773369663530](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369663530.png)

```
# 导入OpenCV的库
import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接使用函数去进行中值滤波
image_median = cv2.medianBlur(image_np, 3)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_median', image_median)
cv2.waitKey(0)
```

### 14.5 双边滤波

![1773369707795](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369707795.png)

![1773369811519](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369811519.png)

![1773369821215](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369821215.png)

```
# 导入OpenCV的库
import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./lena.png')

# 2. 直接进行双边滤波
image_bil = cv2.bilateralFilter(image_np, 5, 150, 150)

cv2.imshow('image_np', image_np)
cv2.imshow('image_bil', image_bil)
cv2.waitKey(0)
```

### 14.6 小结

![1773369852937](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773369852937.png)

## 15. 图像梯度处理

![1773373278908](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773373278908.png)

### 15.1 垂直边缘提取

![1773373361174](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773373361174.png)

​	==这个算子可以自己手动设置。==

```
# 导入OpenCV库
import cv2
import numpy as np

# 1. 图像输入
image_np = cv2.imread('./shudu.png')

# 构建卷积核
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

# 2. 进行梯度处理
image_filter2D = cv2.filter2D(image_np, -1, kernel)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_filter2D', image_filter2D)
cv2.waitKey(0)
```

### 15.2 Sobel算子

![1773373478045](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773373478045.png)

```
# 导入OpenCV库
import cv2
import numpy as np

# 1. 图像输入
image_np = cv2.imread('./test.png')

image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 2. 进行卷积运算
image_Sobel = cv2.Sobel(image_np, -1, 1, 0)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Sobel', image_Sobel)
cv2.waitKey(0)
```

### 15.3 Laplacian算子

![1773373542386](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773373542386.png)

```
# 导入OpenCV库
import cv2
import numpy as np

# 1. 图像输入
image_np = cv2.imread('./shudu.png')

# 2. 进行卷积
image_Laplacian = cv2.Laplacian(image_np, -1)

# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Laplacian', image_Laplacian)
cv2.waitKey(0)
```

## 16.图像边缘检测

![1773388265849](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773388265849.png)

### 16.1 高斯滤波

![1773388298869](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773388298869.png)

### 16.2 计算图像的梯度和方向

![1773388434577](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773388434577.png)

### 16.3 非极大值抑制

![1773388517186](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773388517186.png)

### 16.4 双阈值筛选

![1773388577264](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1773388577264.png)

```
# 导入OpenCV库，方便调用函数
import cv2

# 1. 读取图像
image_np = cv2.imread('./picture.png')

# 2. 灰度化图像
image_np1 = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 高斯滤波
image_blur = cv2.GaussianBlur(image_np1, (5, 5), 1.5)

# 4. 进行边缘检测
image_canny = cv2.Canny(image_blur, 30, 70)

# 5. 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_canny', image_canny)
cv2.waitKey(0)
```

## 17.绘制图像轮廓

