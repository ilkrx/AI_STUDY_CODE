import numpy as np
import matplotlib.pyplot as plt
# 计算正弦曲线上的点的x和y坐标
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
# 创建一个颜色数组，基于y值映射到颜色
colors = y
# 绘制散点图，添加所有属性
plt.scatter(x, y,
            s=10,
            c=colors,
            marker='o',
            cmap='viridis',
            norm=None,
            vmin=-1,
            vmax=1,
            alpha=0.5,
            )
 # 添加颜色条
plt.colorbar()
 # 散点的大小
# 散点的颜色，这里使用y值映射颜色
# 散点的标记样式
# 颜色映射
# 默认的标准化
# 颜色映射的最小值
# 颜色映射的最大值
# 透明度
linewidths=0.5,
edgecolors='w'
# 显示图形
plt.show()
# 散点边缘的线宽
# 散点边缘的颜色