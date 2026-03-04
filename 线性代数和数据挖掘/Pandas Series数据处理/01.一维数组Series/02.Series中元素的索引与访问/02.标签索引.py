import pandas as pd

Series1 = pd.Series([10,20,30,40,50],index=['a','b','c','d',0])

print(Series1)
print(Series1['c'])
print(Series1[0])