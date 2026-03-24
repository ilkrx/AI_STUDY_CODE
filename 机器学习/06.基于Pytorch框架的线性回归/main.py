import matplotlib.pyplot as plt
import torch
import torch.nn as nn  # "nn" 是 "Neural Network"（神经网络）的缩写

"""
    全连接层（nn.Linear）
    卷积层（nn.Conv2d、nn.Conv1d 等）
    池化层（nn.MaxPool2d、nn.AvgPool2d 等）
    循环神经网络层（nn.RNN、nn.LSTM、nn.GRU）
    归一化层（nn.BatchNorm2d、nn.LayerNorm 等）
    dropout 层（nn.Dropout）等
"""
# 1、散点输入
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6],
        [0.4, 34.0], [0.8, 62.3]]

data = torch.tensor(data, dtype=torch.float32)

# 提取x,y
xs = data[:, 0].reshape(-1, 1)

ys = data[:, 1].reshape(-1, 1)

# 定义全连接层
# model = nn.Linear(1,1) # 输入1个特征，输出1个结果

# 1)nn.Sequential是pytorch的一个模块容器，按顺序组合多个网络层
# nn.Sequential默认带forward方法
# forward方法会定义模型的前向传播逻辑，给定输入，经过逻辑，得到输出
# model = nn.Sequential(
#     nn.Linear(1, 1)  # 输入1个特征，输出1个结果
# )

# 2)nn.ModuleList
"""
demo:
# 定义一个继承自 nn.Module 的神经网络基类  
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        # 定义网络层
        self.fc1 = nn.Linear(784, 256)  # 全连接层：输入784维，输出256维
        self.relu = nn.ReLU()           # ReLU激活函数
        self.fc2 = nn.Linear(256, 10)   # 全连接层：输出10维（对应10个类别）
        self.softmax = nn.Softmax(dim=1) # Softmax激活（用于分类概率输出）

    # 定义前向传播过程
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

    # 创建模型实例
    model = SimpleNet()
    print(model)
"""


# 定义一个继承自 nn.Module 的神经网络基类
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 定义网络层
        self.fc1 = nn.Linear(1, 1)  # 全连接层

    # 定义前向传播过程
    def forward(self, x):
        x = self.fc1(x)
        return x


# 创建模型实例
model = LinearModel()
print(model)

# 3、 定义损失函数和优化器
loss_fn = nn.MSELoss()  # 均方误差损失函数 fn-函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 奥普踢麦泽
# 获取模型参数   一个神经元对应两个参数 权重和偏置
# for param in model.parameters():
#     print(param)

# 4、开始迭代
epoches = 100

for i in range(epoches):
    # 梯度清零
    optimizer.zero_grad()
    # 前向传播
    y_pred = model(xs)
    # 计算损失
    loss = loss_fn(y_pred, ys)
    # 反向传播
    loss.backward()
    # 更新参数
    optimizer.step()

    # 获取参数  一般不需要获取
    w = float(model.fc1.weight.data)
    b = float(model.fc1.bias.data)
    if i % 10 == 0:
        print(f'epoch {i} loss: {loss.item()}')

    plt.clf()
    plt.scatter(xs, ys, label='rawdata')
    plt.plot(xs, y_pred.tolist(), 'r-', label=f'y={w:.2f}x+{b:.2f}')
    plt.legend()
    plt.pause(0.5)