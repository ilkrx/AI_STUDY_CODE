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

