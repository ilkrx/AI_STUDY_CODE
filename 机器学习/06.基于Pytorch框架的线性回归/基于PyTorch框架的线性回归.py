import torch
import numpy as np
import torch.nn as nn


# 设置随机数种子
# 作用：确保每次初始位置w相同
# seed = 10
# torch.manual_seed(seed)
#
# tensor1 = torch.rand((3,4))
#
# print(tensor1)

# 1.散点输入
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]]

# 将data中的x和y分别取出来，转化成numpy数组方便取出
data = np.array(data)
x_data = data[:,0]
y_data = data[:,1]
# print(x_data)
# print(y_data)

# pytorch中数据类型需要tensor,因此需要将散点转化成tensor
x_train = torch.tensor(x_data,dtype=torch.float32)
y_train = torch.tensor(y_data,dtype=torch.float32)
print(x_train)
print(y_train)

# 设置随机数种子
seed = 10
torch.manual_seed(seed)

# 2.定义前向模型
# model = nn.Linear(1,1)      # 输入特征是1，输出特征是1    ------>    表示只有一个输入特征x，只有一个输出特征y

# 1)nn.Sequential是pytorch的一个模块容器，按顺序组合多个网络层
# nn.Sequential默认带forward方法
# forward方法会定义模型的前向传播逻辑，给定输入，经过逻辑，得到输出
# model = nn.Sequential(nn.Linear(1, 1))

# 2)nn.ModuleList

# model = nn.ModuleList([nn.Linear(1, 1)])
# class LinearModel(nn.Module):
#     def __init__(self):
#         super(LinearModel, self).__init__()
#         self.layers = nn.ModuleList([nn.Linear(1, 1)])
#
#     def forward(self, x):
#         for layer in self.layers:
#             x = layer(x)
#         return x
#
# model = LinearModel()

# 3)nn.ModuleDict
# nn.ModuleDict：可以给每个层自定义名字
#  nn.ModuleList：不可以给每个层自定义名字
# model = nn.ModuleDict({"linear": nn.Linear(1, 1)})
# class LinearModel(nn.Module):
#     def __init__(self):
#         super(LinearModel, self).__init__()
#         self.layers = nn.ModuleDict({"linear": nn.Linear(1, 1)})
#
#     def forward(self, x):
#         for layer in self.layers.values():
#             x = layer(x)
#         return x
#
# model = LinearModel()

"""
实际上最常用的
"""
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)
        self.linear2 = nn.Linear(2, 1)

    def forward(self, x):
        x = self.linear(x)
        return x

model = LinearModel()


# 3.定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)


# 4.开始迭代
epochs = 500
for epoch in range(1,epochs + 1):
    y_hat = model(x_train.unsqueeze(1)) # （10，1）  (batch_size, in_features)

    # 计算损失
    loss = criterion(y_hat.squeeze(1),y_train)  # (1,)

    # 作用：清空之前存储在优化器中的梯度
    optimizer.zero_grad()

    # 计算损失函数关于参数模型的梯度
    loss.backward()

    # 根据优化算法更新参数
    optimizer.step()

    # 5.显示频率设置
    if epoch % 10 == 0 or epoch == 1:
        print(f"epochs:{epoch},loss:{loss}")