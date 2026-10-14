import pandas as pd

# ==========
# F/M 有很多并列值(如 F=1 一大把人), 直接 qcut 会报 Bin edges must be unique
# 用 .rank(method='first') 先排名再切, 保证每层人数严格相等(四分位）

print('===== S1: 读清洗后数据 + snapshot =====')
df = pd.read_csv('data/online_retail_cleaned.csv')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])   # CSV 不保存类型, 读回要重新转
snapshot = df['InvoiceDate'].max() + pd.Timedelta(days=1)
#**
print('清洗后数据:', len(df), '行 | 快照日:', snapshot, '\n')

print('===== S2: 按客户聚合 RFM 三指标 =====')
rfm = df.groupby('Customer ID').agg(R_lastdate=('InvoiceDate', 'max'),   # 最后购买时间
                                    F=('Invoice', 'nunique'),            # 去重订单数
                                    M=('Amount', 'sum'))                 # 累计金额
rfm['R'] = (snapshot - rfm['R_lastdate']).dt.days   # R = 距今天数
rfm = rfm.drop(columns=['R_lastdate'])              # 中间列用完即删
print('客户总数:', len(rfm))
print(rfm.describe().round(1), '\n') 

print('===== S3: 四分位打分 + 八分层 =====')
# R 越小越好 → 排名后标签倒序(1~4, 4=最近); F/M 越大越好 → 正序(4=最频繁/最高消费)
rfm['R_score'] = pd.qcut(rfm['R'].rank(method='first'),    4, labels=[4, 3, 2, 1]).astype(int)
rfm['F_score'] = pd.qcut(rfm['F'].rank(method='first'),    4, labels=[1, 2, 3, 4]).astype(int)
rfm['M_score'] = pd.qcut(rfm['M'].rank(method='first'),    4, labels=[1, 2, 3, 4]).astype(int)
#**int方便比较

print(rfm.head())
# 高低二元化后组合成 8 个客群 (1=高, 0=低), 顺序 = (R, F, M)
seg_map = {
    (1, 1, 1): '重要价值客户',   # 最近来、常来、花得多 → 重点维护
    (1, 0, 1): '重要发展客户',   # 最近来、花得多、但不频繁 → 提频
    (0, 1, 1): '重要保持客户',   # 常来花得多、但最近没来 → 防流失
    (0, 0, 1): '重要挽留客户',   # 花得多、但不常来且很久没来 → 召回
    (1, 1, 0): '一般价值客户',
    (1, 0, 0): '一般发展客户',
    (0, 1, 0): '一般保持客户',
    (0, 0, 0): '一般挽留客户',
}
rfm['segment'] = rfm.apply(
    lambda r: seg_map[(r.R_score >= 3, r.F_score >= 3, r.M_score >= 3)], axis=1)
#**

print(rfm.head())
# 汇总表: 每个客群的人数/占比/贡献金额/金额占比 (md笔记)
summary = rfm.groupby('segment').agg(人数=('M', 'size'),
                                     贡献金额=('M', 'sum'))
summary['人数占比%'] = (summary['人数'] / summary['人数'].sum() * 100).round(1)
summary['金额占比%'] = (summary['贡献金额'] / summary['贡献金额'].sum() * 100).round(1)
print(summary.sort_values('贡献金额', ascending=False), '\n')
#**

rfm.to_csv('data/rfm.csv')
print('已导出 data/rfm.csv')
