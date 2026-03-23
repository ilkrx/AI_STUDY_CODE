import torch

# 打印一个标量
scalar_tensor = torch.tensor(3.14)
print(scalar_tensor)

# 打印一个向量
vector_tensor = torch.tensor([1,2,3,4,5,6])
print(vector_tensor)

# 打印一个矩阵
matrix_tensor = torch.tensor([[1,2,3],[4,5,6]])
print(matrix_tensor)

"""
    tensor的存储
"""
tensor1 = torch.tensor([[1,2,3],[4,5,6]])
# 打印张量
print(tensor1)

# 打印形状
print(tensor1.shape)

# 数据类型
print(tensor1.dtype)

# 存储的内容
print(tensor1.storage().tolist())

"""
    storage的存储
"""
tensor2 = torch.arange(12).reshape(3,4)
print(tensor2.storage().tolist())

# 转置
tensor3 = tensor2.T
print(tensor3.storage().tolist())
print(tensor3.storage().data_ptr())

# 步长
print(tensor2.stride())

"""
    连续性
"""
a = torch.arange(12).reshape(3, 4)
# print(a.flatten())
# # print(a.storage().tolist())
b = a.transpose(0, 1)
# print(b.flatten())
# print(b.storage().tolist())
print(b.is_contiguous())
b = b.contiguous()
print(b.is_contiguous())
print(b.view(2, 6))