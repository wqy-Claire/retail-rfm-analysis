import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'PingFang SC'

df = pd.read_csv('data/online_retail_cleaned.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ===== S0 画图前的时间边界检查 =====
# 月度趋势图最容易把"数据不完整"误读成"业务暴跌"
# 验证逻辑：如果最后一个月覆盖天数远少于 28~31 天, 该月柱子/折点必须标注"不完整"
print('====S0: 时间边界检查====')
print('数据范围:', df['InvoiceDate'].min(), '->', df['InvoiceDate'].max())
last_month = df[df['InvoiceDate'] >= '2011-12-01']
print('最后一个月(2011-12)覆盖到的最大日期:', last_month['InvoiceDate'].max())
print('结论: 2011-12 只有前 9 天数据, 是不完整月\n')

print('====图 1：月度销售额趋势====')
monthly = df.set_index('InvoiceDate').resample('ME')['Amount'].sum()
print(monthly.index.min(), '->', monthly.index.max()) 

plt.figure(figsize=(10,5))
plt.plot(monthly.index, monthly.values)
plt.title('月度销售额趋势（2009-2011）')
plt.xticks(rotation = 45)
plt.tight_layout() #防止截断
plt.savefig('figures/monthly_trend.png',dpi = 150, bbox_inches='tight')  #保存裁边
plt.show()

print('====图 2：八分层金额占比====')
rfm = pd.read_csv('data/rfm.csv')
seg_rev = rfm.groupby('segment')['M'].sum().sort_values()
plt.figure(figsize=(10,5))
plt.bar(seg_rev.index, seg_rev.values)
plt.title('RFM 八分层贡献金额')
plt.tight_layout()
plt.savefig('figures/segment_revenue.png',dpi = 150,bbox_inches='tight')
plt.show()

print('====图 3：国家 Top10====')
country = df.groupby('Country')['Amount'].sum().sort_values().tail(10) # 小到大

plt.figure(figsize=(10,5))
plt.barh(country.index, country.values)
plt.title('国家 Top10 销售额')
plt.tight_layout()
plt.savefig('figures/country_top10.png',dpi = 150,bbox_inches='tight')
plt.show()

# ===== 补充 =====
uk_share = df[df['Country'] == 'United Kingdom']['Amount'].sum() / df['Amount'].sum()
print(f'英国销售额占比: {uk_share:.1%}')