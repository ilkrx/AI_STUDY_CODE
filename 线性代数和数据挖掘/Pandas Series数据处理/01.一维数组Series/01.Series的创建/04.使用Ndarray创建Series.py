import pandas as pd
import numpy as np

arr = np.array([1,2,3,4,5])

# copy参数设置False时会改变Ndarray原始数据
Series1 = pd.Series(arr,dtype=float)  #  ,copy=False
Series1[0] = 10
print(Series1)
print(arr)