import pandas as pd
#读入数据
df = pd.read_csv('data/online_retail_II.csv')
#数据体检
print('df（行，列）：')
print(df.shape)
print('df的列状态是：')
print(df.dtypes)
print('df的前几行是：')
print(df.head())
print('df空缺值个数')
print(df.isnull().sum())
print('df重复行数')
print(df.duplicated().sum())
print('df的描述')
print(df.describe())
