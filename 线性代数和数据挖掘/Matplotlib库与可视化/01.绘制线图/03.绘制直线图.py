import numpy as np

import matplotlib.pyplot as plt

x = np.array([0,5])

y = np.array([0,10])

plt.plot(x, y, '-',
         label='Line between two points',    # 图例标签
         linewidth=2,   # 线宽
         color='red',   # 线的颜色
         marker='o',  # 标记样式
         markersize=5,  # 标记的大小
         markeredgecolor='black',  # 标记边缘的颜色
         markeredgewidth=1,  # 标记边缘的宽度
         markerfacecolor='none',  # 标记内部的颜色
         alpha=0.5 # 透明度
         )
plt.legend()
plt.show()