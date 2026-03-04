import pandas as pd

# 使用字典创建DataFrame，键作为列名
# 字典的值为列表、数组等可迭代对象，要求：长度要一致！
data = {
    'name':['Tom','Nick','John'],
    'age':[19,20,21]
}

df = pd.DataFrame(data)

print(df)