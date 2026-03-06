import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

# 读取文件
score_data = pd.read_excel('source.xlsx')

# 有缺失数据，需要对文件进行数据清洗
# 用0代表缺失数据，表示学生成绩为0
score_data.fillna(0,inplace=True)   # 设置inplace参数修改score_data，不创建新的DataFrame
# print(score_data)

# 计算最终成绩：最终成绩 = 平时成绩 * 0.3 + 考试成绩 * 0.7
# 平时成绩
attendance = score_data['attendance'].values    # values属性  ->  数组形式
# print(type(attendance))
# print(attendance.shape)
# 考试成绩
exam = score_data['exam'].values
# 最终成绩:对其四舍五入
final_score = np.round(attendance * 0.3 + exam * 0.7)
# print(final_score.shape)
# print(final_score)

# 将数组转换成DataFrame对象
final_score_df = pd.DataFrame(final_score,columns=['final_score'])
# print(final_score_df)

# 判断最终成绩是否及格(whether_passed)
# 首先默认都不及格，然后修改
final_score_df['whether_passed'] = '不及格'
final_score_df.loc[final_score_df['final_score'] >= 60,'whether_passed'] = '及格'

# print(final_score_df)
# print(type(final_score_df))

# 拼接final_score_df和score_data
final_data = pd.concat([score_data,final_score_df],axis=1)
print(final_data)

final_data.to_excel('final_source.xlsx')

# 使用Matplotlib显示最终成绩和及格率
# 最终成绩用条形图
x = np.arange(0,110,10)
# 使用np.histogram函数计算每个区间的学生人数
hist, bin_edges = np.histogram(final_data['final_score'], bins=x)
print(hist)
print(bin_edges)
# 计算条形图的宽度
bar_width = (bin_edges[1] - bin_edges[0])
# 绘制条形图，x轴是分数区间，y轴是学生人数
plt.bar(bin_edges[:-1], hist, width=bar_width, align='edge')
# 在每个条形图上添加文本，显示该区间内的学生人数
for i in range(len(hist)):
    if hist[i]:  # 如果该区间有学生，则添加文本
        plt.text(bin_edges[i] + bar_width / 2, hist[i] + 0.1, str(hist[i]), ha='center')
# 设置图表的标题和坐标轴标签
plt.title('finally')
plt.xlabel('score')
plt.ylabel('number')
# plt.bar(x,hist)
plt.show()
# 及格率用饼图
# 使用value_counts方法统计通过和未通过的学生数量
pass_count = final_data['whether_passed'].value_counts()
print(pass_count)
# 绘制饼图，显示通过和未通过的比例
plt.pie(pass_count, labels=pass_count.index, autopct='%1.1f%%')
# 设置饼图的标题
plt.title('Distribution of Passing Status')
# 显示饼图
plt.show()