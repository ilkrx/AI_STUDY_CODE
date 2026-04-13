import os
import random

import numpy as np

import torch
from torch import nn
import torchvision
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt  # 修正1：应该是 matplotlib.pyplot，不是 matplotlib as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns


# 1、设置随机数种子
def setup_seed(seed):
    # numpy的随机数种子
    np.random.seed(seed)
    # python的随机数种子
    random.seed(seed)
    # python的哈希种子
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        # 设置cuda随机数种子
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        # 关闭cudnn加速
        torch.backends.cudnn.benchmark = False
        # 设置cudnn为确定性算法
        torch.backends.cudnn.deterministic = True  # 修正2：补充完整的确定性设置


# 设置随机数种子
setup_seed(0)

# 检查GPU、CUDA是否可用，如果可用就使用GPU，否则使用CPU
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available, using GPU.")  # 修正3：冒号后加空格
else:
    device = torch.device("cpu")
    print("CUDA is not available, using CPU.")

# 2、定义数据集的加载与处理

# 定义训练数据的处理步骤
train_transforms = transforms.Compose(
    [
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(0.5),
        # 修正4：删除了 CenterCrop(224)，因为 RandomResizedCrop 已经裁剪到224了
        # 重复裁剪会进一步缩小图像，影响训练效果
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]
)

# 定义验证数据的处理步骤
valid_transforms = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]
)

# 加载数据
train_datasets = datasets.ImageFolder("../DataSet/train", transform=train_transforms)
valid_datasets = datasets.ImageFolder("../DataSet/val", transform=valid_transforms)

# 做成dataloader，方便后续模型训练
train_dataloader = DataLoader(train_datasets, batch_size=32, shuffle=True)
valid_dataloader = DataLoader(valid_datasets, batch_size=32, shuffle=True)

# 3、定义模型
model = torchvision.models.resnet34(weights=None).to(device)

model.load_state_dict(torch.load('../Model/resnet34-b627a593.pth', weights_only=True))

for param in model.parameters():
    param.requires_grad = False

fc_inputs = model.fc.in_features
model.fc = nn.Sequential(
    nn.Linear(fc_inputs, 256),
    nn.ReLU(),
    nn.Dropout(0.4),
    nn.Linear(256, 52),
    # 修正5：如果使用 CrossEntropyLoss，不需要 LogSoftmax
    # CrossEntropyLoss 内部已经包含了 Softmax
    # nn.LogSoftmax(dim=1),
).to(device)

# 4、定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # 修正6：拼写错误 optimtizer -> optimizer

# 5、训练模型
epochs = 100
best_acc = 0  # 修正7：most_acc 应该在循环外定义，否则每个epoch都会重置为0

for epoch in range(epochs):
    model.train()
    total_loss = 0

    for i, (images, labels) in enumerate(train_dataloader):
        images = images.to(device)
        labels = labels.to(device)

        # 梯度清零
        optimizer.zero_grad()

        # 前向传播
        outputs = model(images)

        # 计算损失
        loss = criterion(outputs, labels)

        # 反向传播
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        # 修正8：减少打印频率，避免输出过多
        if (i + 1) % 50 == 0:
            print(f'Epoch [{epoch + 1}/{epochs}] Batch [{i + 1}/{len(train_dataloader)}] Loss {loss.item():.4f}')

    avg_loss = total_loss / len(train_dataloader)
    print(f'Epoch [{epoch + 1}/{epochs}] Training Loss: {avg_loss:.4f}')

    # 验证阶段
    model.eval()
    correct = 0
    total = 0
    total_loss = 0  # 修正9：重名问题，改为 val_loss

    with torch.no_grad():
        for images, labels in valid_dataloader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)  # 修正10：test_loss -> loss
            total_loss += loss.item()  # 修正11：使用 .item() 获取数值
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    avg_val_loss = total_loss / len(valid_dataloader)
    acc = correct / total
    print(f"Validation: Epoch [{epoch + 1}/{epochs}], Loss: {avg_val_loss:.4f}, Accuracy: {acc * 100:.2f}%")

    # 保存最佳模型
    if acc > best_acc:
        best_acc = acc
        torch.save(model.state_dict(), f"../Model/model_best.pth")
        print(f"  -> 保存最佳模型，准确率: {best_acc * 100:.2f}%")

    # 每10个epoch保存一次检查点
    if (epoch + 1) % 10 == 0:
        torch.save(model.state_dict(), f"../Model/model_{epoch + 1}.pth")

print(f"\n训练完成！最佳验证准确率: {best_acc * 100:.2f}%")

# 6、最终测试
model.eval()

correct = 0
total = 0
predicted_labels = []
true_labels = []

with torch.no_grad():
    for images, labels in valid_dataloader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        predicted_labels.extend(predicted.cpu().numpy())
        true_labels.extend(labels.cpu().numpy())

print(f'Final accuracy on validation set: {100 * correct / total:.2f}%')

# 可视化，绘制混淆矩阵
plt.figure(figsize=(14, 12))  # 修正12：52类需要更大的图
conf_matrix = confusion_matrix(true_labels, predicted_labels)

# 修正13：对于52类，annot=True会导致数字重叠，建议关闭
sns.heatmap(conf_matrix, annot=False, fmt='d', cmap='Blues', cbar=True)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()