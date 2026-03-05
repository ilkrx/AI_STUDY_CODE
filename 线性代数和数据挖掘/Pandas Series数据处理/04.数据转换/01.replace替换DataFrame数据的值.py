import pandas as pd

df = pd.DataFrame(
    {
        'A':[1,2,3,4,5],
        'B':['a','b','c','d','e']
    }
)

print(df)
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 单一值替换
new_df = df.replace(2,10)

print(new_df)

# 列表替换所有匹配值
new_df1 = df.replace([2,3,'a'],'z')
print(new_df1)

# 字典替换
c_dict = {
    2:200,
    'b':'y'
}
new_df2 = df.replace(c_dict)
print(new_df2)

# 使用正则表达式替换
df = pd.DataFrame({
    'col1': ['apple', 'banana', 'cherry', 'agerape', 'apricote'],
    'col2': ['apple pie', 'banana split', 'cherry tart', 'grape juice', 'apricote jam']
})

res = df.replace(r'^a.*e$','fruit',regex=True)  # regex参数默认为False，只有当使用正则表达式替换时一定要设置regex参数
print(res)