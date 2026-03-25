import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 1.数据预处理
data = pd.read_excel("Real estate valuation data set.xlsx")
# 判断有没有读进来数据
# print(data.head())

# 处理数据：连续型数据和离散型数据
# 注意：离散型数据处理    ------>     one-hot编码处理：
data = pd.get_dummies(data,columns=['X4 number of convenience stores'])
# print(data.columns)
x_data = data[['X1 transaction date','X2 house age','X3 distance to the nearest MRT station','X5 latitude','X6 longitude','X4 number of convenience stores_0',
       'X4 number of convenience stores_1',
       'X4 number of convenience stores_2',
       'X4 number of convenience stores_3',
       'X4 number of convenience stores_4',
       'X4 number of convenience stores_5',
       'X4 number of convenience stores_6',
       'X4 number of convenience stores_7',
       'X4 number of convenience stores_8',
       'X4 number of convenience stores_9',
       'X4 number of convenience stores_10']]
y_data = data['Y house price of unit area']
# print(x_data)
# print(y_data)


# 先划分训练集和测试集 再进行标准化
# 划分训练集和测试集  test_size和train_size只需要指定一个就行
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2,random_state=10)
# 进行标准化
# 注意：标准化返回的结果已经是个数组
scale = StandardScaler()
x_train_scaled = scale.fit_transform(x_train)
# print(x_train_scaled)
x_test_scaled = scale.transform(x_test)

# 转化成tensor
x_train_tensor = torch.tensor(x_train_scaled,dtype=torch.float32)
x_test_tensor = torch.tensor(x_test_scaled,dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values,dtype=torch.float32).view(-1,1)
y_test_tensor = torch.tensor(y_test.values,dtype=torch.float32).view(-1,1)
print(x_train_tensor.shape)


# # 2.模型定义
class linear_regression(nn.Module):
    def __init__(self,input_size):
        super().__init__()
        self.linear = nn.Linear(input_size,1)

    def forward(self,x):
        x = self.linear(x)
        return x

# 实例化模型
model = linear_regression(x_train_tensor.shape[1])

# 3.定义损失函数和优化器
criterion = nn.MSELoss()
# 优化器
optimizer = optim.Adam(model.parameters(),lr = 0.1)

# 4.开始迭代
epochs = 1000
for epoch in range(0,epochs):
    # 将模式设置成训练模式
    model.train()

    # 删除优化器中的梯度记录
    optimizer.zero_grad()
    # 前向模型
    y_predict = model(x_train_tensor)
    # 计算损失值
    loss = criterion(y_predict,y_train_tensor)
    # 反向模型
    loss.backward()
    # 更新参数
    optimizer.step()

    # 设置提示信息，每隔一段时间得到w和损失值
    if (epoch + 1) % 100 ==0:
        print(f"epoch:{epoch + 1},loss:{loss.item():.4f}")

# 5.评估模型
model.eval()

with torch.no_grad():
    predict = model(x_test_tensor)
    print(predict)
    # 计算测试集上的损失，用于评估模型在未知数据上的表现
    test_loss = criterion(predict, y_test_tensor)
    print(test_loss)