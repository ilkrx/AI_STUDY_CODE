import pandas as pd
import openpyxl

df = pd.read_csv('sales.csv',nrows=6)
df['日期'] = pd.to_datetime(df['日期'])
print(df)

df = pd.read_csv('sales.csv')
print(df)
count_nonan = df.count(numeric_only = True)
print(count_nonan)

sum_nonan = df.sum(numeric_only = True)
print(sum_nonan)

mean_nonan = df.mean(numeric_only = True)
print(mean_nonan)

median_nonan = df.median(numeric_only = True)
print(median_nonan)

min_nonan = df.min(numeric_only = True)
print(min_nonan)

max_nonan = df.max(numeric_only = True)
print(max_nonan)

dict1 = {
    '非NaN值数量':count_nonan,
    '每列总和':sum_nonan,
    '每列平均值':mean_nonan,
    '每列中位数':median_nonan,
    '每列最小值':min_nonan,
    '每列最大值':max_nonan
}
print(dict1)
df1 = pd.DataFrame(dict1)

print(df1)
# df.to_excel('sales_analysis.xlsx',sheet_name='原始数据',index=False)
# df1.to_excel('sales_analysis.xlsx',sheet_name='分析结果',index=False)
with pd.ExcelWriter('sales_analysis.xlsx') as writer:
    df.to_excel(writer, sheet_name='原始数据',index=False)
    df1.to_excel(writer, sheet_name='分析结果',index=False)
