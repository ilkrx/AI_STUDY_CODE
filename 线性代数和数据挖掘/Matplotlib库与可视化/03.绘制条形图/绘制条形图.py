import matplotlib.pyplot as plt
 # 数据
labels = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]
 # 创建条形图，并添加关键字参数
plt.bar(labels, values,
        width=0.3,       # 条形的宽度
        bottom=0,
        align='edge',  # 条形与x位置的对齐方式
        data=None,
        color='r',  # 条形的填充颜色, 和facecolor等价
        edgecolor='r',   # 条形边缘的颜色
        # facecolor = 'g', # 填充颜色
        linewidth=2,     # 条形边缘的线宽
        linestyle='-',   # 条形边缘的线型
        alpha=0.7,       # 条形的透明度
        # hatch='x',       # 条形的填充图案
        log = False,     # 条形的高度不以对数尺度表示。
        label='test'     # 为条形创建图例时使用的标签
       )
# 显示图例
plt.legend()

# 显示图表
plt.show()
