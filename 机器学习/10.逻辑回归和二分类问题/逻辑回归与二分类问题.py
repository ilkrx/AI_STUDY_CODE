import numpy as np
import matplotlib.pyplot as plt

# 1.散点输入
class1_points = np.array([[1.9, 1.2],
                          [1.5, 2.1],
                          [1.9, 0.5],
                          [1.5, 0.9],
                          [0.9, 1.2],
                          [1.1, 1.7],
                          [1.4, 1.1]])

class2_points = np.array([[3.2, 3.2],
                          [3.7, 2.9],
                          [3.2, 2.6],
                          [1.7, 3.3],
                          [3.4, 2.6],
                          [4.1, 2.3],
                          [3.0, 2.9]])
# 提取两类特征，输入特征维度为2
x1_data = np.concatenate((class1_points[:, 0], class2_points[:, 0]))
x2_data = np.concatenate((class1_points[:, 1], class2_points[:, 1]))
# 两类点打标签
label = np.concatenate((np.zeros(len(class1_points)), np.ones(len(class2_points))))


# 2.前向计算
def forward(w1, w2, b):
    z = w1 * x1_data + w2 * x2_data + b
    a = sigmoid(z)
    return a


# 3.sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 4.参数初始化
w1 = 0.1
w2 = 0.1
b = 0
lr = 0.05


# 5.损失函数
def loss_func(a):
    loss = -np.mean(label * np.log(a) + (1 - label) * np.log(1 - a))
    return loss


fig, (ax1, ax2) = plt.subplots(2, 1)
epoch_list = []
loss_list = []

# 6.开始迭代
epoches = 1000
for epoch in range(1, epoches + 1):
    # 7.反向传播
    a = forward(w1, w2, b)
    deda = (a - label) / (a * (1 - a))
    dadz = a * (1 - a)

    dzdw1 = x1_data
    dzdw2 = x2_data
    dzdb = 1

    gradient_w1 = np.dot(dzdw1, (deda * dadz)) / len(x1_data)
    gradient_w2 = np.dot(dzdw2, (deda * dadz)) / len(x2_data)
    gradient_b = (deda * dadz * dzdb).sum() / len(x1_data)

    w1 -= lr * gradient_w1
    w2 -= lr * gradient_w2
    b -= lr * gradient_b

    # 8.显示频率设置
    if epoch % 50 == 0 or epoch == 1:
        # 计算损失
        a = forward(w1, w2, b)
        loss = loss_func(a)
        print(loss)