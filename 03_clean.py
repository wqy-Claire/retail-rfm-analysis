import pandas as pd
#读入数据
df = pd.read_csv('data/online_retail_II.csv')
print('数据已读取，共', len(df), '行\n')

#R1:删除完全重复行
before = len(df)
df = df.drop_duplicates()
print(f'R1 删除重复行 {before - len(df)} 行, 剩余 {len(df)} 行\n')

#R2:拆出退货单(C开头), 单独保存暂不分析
before = len(df)
returns = df[df['Invoice'].str.startswith('C')]
df = df[~df['Invoice'].str.startswith('C')]
print(f'R2 拆出退货单 {before - len(df)} 行, 剩余 {len(df)} 行\n')

# **R3:删除非商品服务行(邮费/手工单/调账等非商品记录)
before = len(df)
service_mask = df['StockCode'].isin(['POST', 'DOT', 'M', 'm', 'C2', 'PADS']) \
               | df['Description'].isin(['BANK CHARGES', 'CRUK Commission'])
df = df[~service_mask]
print(f'R3 删除非商品服务行 {before - len(df)} 行, 剩余 {len(df)} 行\n')

#R4:删除Price<=0(赠品/冲销, 不产生销售额; 非C负数量单全在这里被带走)
print('清洗前负数量行数:', (df['Quantity'] <= 0).sum())
before = len(df)
df = df[df['Price'] > 0]
print(f'R4 删除Price<=0 {before - len(df)} 行, 剩余 {len(df)} 行\n')
print('清洗后负数量行数(应为0):', (df['Quantity'] <= 0).sum())

#R5:删除Customer ID缺失(无法定位用户）
before = len(df)
df = df.dropna(subset=['Customer ID'])
print(f'R5 删除ID缺失 {before - len(df)} 行, 剩余 {len(df)} 行\n')

#R6:类型修正 + 新增Amount列
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Customer ID'] = df['Customer ID'].astype(str)
df['Amount'] = df['Quantity'] * df['Price']

#清洗后体检: 负数量应为0
print('清洗完成, 最终', len(df), '行\n')

#保存
returns.to_csv('data/returns.csv', index=False)
df.to_csv('data/online_retail_cleaned.csv', index=False)
