import pandas as pd
#读入数据
df = pd.read_csv('data/online_retail_II.csv')
print('数据已读取，共', len(df), '行\n')
#数据清洗前的数据观察

print('检查问题4:Quantity, Price < 0')

df1 = df[df['Quantity'] < 0]
df11 = df[df['Quantity'] >= 0]
print('① Quantity < 0 的行数：', len(df1))
print('抽查 5 行：')
print(df1.sample(5), '\n')
print('对比：Quantity异常组df1 vs 正常组df11')
print('df1里 C 开头退货单占比：', df1['Invoice'].str.startswith('C').mean())
print('df11里 C 开头退货单占比：', df11['Invoice'].str.startswith('C').mean())
print()
print('df1里 CustomerID 也缺失占比：', df1['Customer ID'].isnull().mean())
print('df11里 CustomerID 缺失占比：', df11['Customer ID'].isnull().mean())
print('可能原因是退货','\n')

df2 = df[df['Price'] <= 0]
df22 = df[df['Price'] > 0]
print('② Price <= 0 的行数：', len(df2))
print('抽查 5 行：')
print(df2.sample(5), '\n')
print('df2里 Description 缺失的占比：', df2['Description'].isnull().mean())
print('df22里 Description 缺失的占比：', df22['Description'].isnull().mean())
print()
print('df2里 CustomerID 也缺失占比：', df2['Customer ID'].isnull().mean())
print('df22里 CustomerID 缺失占比：', df22['Customer ID'].isnull().mean())
print('Price<=0的行中，description 和 customer id 也多为空 可以删除 customer id NaN 的行','\n')

print('检查问题6:C 开头退货单')
print('C 开头的退货单行数：', df['Invoice'].str.startswith('C').sum(), '\n')
print('检查问题 3：CustomerID 缺失')

print('检查问题3:CustomerID和Description缺失')

df3 = df[df['Customer ID'].isnull()]
print('抽查 5 行：')
print(df3.sample(5), '\n')
print('①CustomerID 缺失行数：', len(df3))
print('缺失行的国家分布（前 10）：')
print(df3['Country'].value_counts().head(10), '\n')
print('全部数据的国家分布（前 10，对比用）：')
print(df['Country'].value_counts().head(10), '\n')
print('与国家无关','\n')

df4 = df[df['Description'].isnull()]     # desc缺失组
print('desc 缺失组抽查 5 行：')
print(df4.sample(5), '\n')
print('②description 缺失行数：', len(df4))
df44= df[df['Description'].notnull()]    # desc完整组
print('对比：Description 缺失组 vs 完整组')
print('缺失组里 C 开头退货单占比：', df4['Invoice'].str.startswith('C').mean())
print('完整组里 C 开头退货单占比：', df44['Invoice'].str.startswith('C').mean())
print()
print('缺失组里 CustomerID 也缺失占比：', df4['Customer ID'].isnull().mean())
print('完整组里 CustomerID 缺失占比：', df44['Customer ID'].isnull().mean())
print('结论：description 缺的行 customer id 一定缺（100%）；但反过来不成立')
# ===== 补充检查（10/14）=====
print('\n===== 补充检查 =====')

# 1) **Quantity<0 且非 C 开头：调整/冲销单的特征
neg = df[df['Quantity'] < 0]
neg_nonC = neg[~neg['Invoice'].str.startswith('C')]
print('Quantity<0 总行数:', len(neg))
print('  其中 C 开头(退货):', neg['Invoice'].str.startswith('C').sum())
print('  其中非 C(调整/冲销):', len(neg_nonC),
      '| 国家:', neg_nonC['Country'].unique(),
      '| Price 范围:', neg_nonC['Price'].min(), '~', neg_nonC['Price'].max())
print('Quantity<0 且非 C 开头的Price均为0，后续分析删掉Price <= 0 可以不用考虑Quantity<0情况 ')
# 2) Price<=0 细分
print('Price<=0 总行数:', (df['Price'] <= 0).sum(),
      '| =0:', (df['Price'] == 0).sum(), '| <0:', (df['Price'] < 0).sum())

# 3) C 开头订单全表数
print('C 开头订单总行数:', df['Invoice'].str.startswith('C').sum())

# 4) 条件概率的正确方向（line61）
id_na = df[df['Customer ID'].isnull()]
print('Customer ID 缺失行里, Description 也缺失的占比:',
      round(id_na['Description'].isnull().mean(), 4))

# 5) 时间范围
print('时间范围:', df['InvoiceDate'].min(), '->', df['InvoiceDate'].max())
print('国家数:', df['Country'].nunique())
