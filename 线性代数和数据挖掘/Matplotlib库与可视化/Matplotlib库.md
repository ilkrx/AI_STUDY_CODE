# Matplotlib库

## 1.Matplotlib库简介

![1772539354415](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772539354415.png)

## 2.Matplotlib库的安装

命令：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib
```

![1772539495784](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772539495784.png)

## 3.线图

![1772586744143](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772586744143.png)

![1772586760619](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772586760619.png)

### 3.1 正弦图像

```
import numpy as np

import matplotlib.pyplot as plt

# 用numpy库生成x坐标和y坐标
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# 使用matplotlib绘制点，并添加属性
plt.plot(x, y, '-',
         label='Sine Wave',    # 图例标签
         linewidth=2,   # 线宽
         color='red',   # 线的颜色
         marker='o',  # 标记样式
         markersize=5,  # 标记的大小
         markeredgecolor='black',  # 标记边缘的颜色
         markeredgewidth=1,  # 标记边缘的宽度
         markerfacecolor='none',  # 标记内部的颜色
         alpha=0.5 # 透明度
         )
# 显示图例
plt.legend()
# 显示图像
plt.show()
```

### 3.2 余弦图像

```
import numpy as np

import matplotlib.pyplot as plt

# 用numpy库生成x坐标和y坐标
x = np.arange(0, 3 * np.pi, 0.1)
y = np.cos(x)

# 使用matplotlib绘制点，并添加属性
plt.plot(x, y, '-',
         label='Sine Wave',    # 图例标签
         linewidth=2,   # 线宽
         color='red',   # 线的颜色
         marker='o',  # 标记样式
         markersize=5,  # 标记的大小
         markeredgecolor='black',  # 标记边缘的颜色
         markeredgewidth=1,  # 标记边缘的宽度
         markerfacecolor='none',  # 标记内部的颜色
         alpha=0.5 # 透明度
         )
# 显示图例
plt.legend()
# 显示图像
plt.show()
```

### 3.3 直线图

```
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
```

## 4.散点图

![1772590065134](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772590065134.png)

```
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
```

## 5.条形图

![1772590539707](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772590539707.png)

```
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
```

## 6.饼图

![1772590839987](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772590839987.png)

```
import matplotlib.pyplot as plt
# 数据
sizes = [25, 35, 20, 21]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
 # 绘制饼图，使用 **kwargs 定制扇形
plt.pie(sizes,                   # 饼图中每个扇形的尺寸
        explode=[0.5, 0, 0, 0],    # 用于指定每个扇形是否突出显示
        labels=labels,           # 用于指定每个扇形的标签
        colors=colors,           # 用于指定每个扇形的颜色
        autopct='%.1f%%',       # 用于在饼图上显示每个扇形的百分比
        startangle=0,          # 饼图开始的角度，默认为 0（即从 x 轴正方向开始）
        shadow=True,            # 用于指定是否为饼图添加阴影
        radius=1,                # 饼图的半径
        wedgeprops=dict(edgecolor='black', linewidth=2, linestyle='-'),  # 指定饼图中每个扇形的属性
        textprops=dict(color='red', weight='bold'),  # 用于指定饼图中标签的文本属性，这里指定文本的颜色和字体的粗细为粗体
        center=(0, 0),            # 用于指定饼图的中心位置
        frame=False,              # 用于指定是否为饼图添加一个坐标轴
        normalize = True ,         # 为True则x中的值将被归一化以使它们的总和等于1
        hatch = 'x'                # 图案填充
)
 # 显示图表
plt.show()
```

## 7.其他常用函数

#### xlabel、ylabel、title、subplot

```
import numpy as np
import matplotlib.pyplot as plt
# 创建数据
x = np.arange(0, 3 * np.pi, 0.01)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 在第一个位置创建子图
plt.subplot(2, 1, 1)  # 2行1列，第一个子图
plt.plot(x, y_sin)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y_sin')
# 在第二个位置创建子图
plt.subplot(2, 1, 2)  # 2行1列，第二个子图
plt.plot(x, y_cos)
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('y_cos')
# 调用 tight_layout  用于自动调整子图（subplot）之间的间距，以避免子图内容被遮挡。它主要解决了当你有多个子图时，子图之间可能会重叠的问题。
plt.tight_layout()
 # 显示图形
plt.show()
```