# Online Retail RFM 用户分层分析

用 Python 对英国电商 106 万条真实订单流水做数据清洗、RFM 用户分层与可视化，回答"谁是核心客户、谁在流失"。

## 背景

- 数据集：[Online Retail II](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)（UCI 公开数据集，2009-12 ~ 2011-12，43 个国家）
- 原始数据 1,067,371 行，清洗后 776,660 行、5,861 个客户
- 数据文件较大未上传仓库，按上述链接下载后放入 `data/` 即可复现

## 主要发现

- **30.8% 的客户贡献了 75.8% 的收入**（重要价值客户 1,806 人 / £1,295 万）
- 重要保持客户 649 人（贡献 £206 万）正在流失，是最优先召回对象
- 销售额呈年末季节性峰值（11-12 月）；英国本土占比 83.7%，海外增长空间大
- 清洗中发现 34,335 行重复录入、19,104 行退货单、4,426 行邮费等非商品记录（详见 m02）

## 方法

1. **数据体检**（`01_eda.py`）：行列数、类型、缺失、重复、异常值
2. **问题诊断**（`02_check.py`）：异常组 vs 正常组对照，验证负数/缺失的成因
3. **数据清洗**（`03_clean.py`）：R1 去重 → R2 拆退货 → R3 删非商品服务行 → R4 删 Price≤0 → R5 删 ID 缺失 → R6 类型修正 + Amount 列（规则与理由见 `m02_cleaning_log.md`）
4. **RFM 分层**（`04_rfm.py`）：按客户聚合 R（最近购买间隔）/ F（去重订单数）/ M（累计金额），四分位打分后组合成 8 个客群（结果见 `m03_rfm_notes.md`）
5. **可视化**（`04_viz.py`）：月度趋势、分层金额、国家 Top10，画图前做时间边界检查防止误读不完整月（图在 `figures/`）

## 复现

```bash
pip install pandas matplotlib
python 03_clean.py   # 需先下载原始数据放入 data/
python 04_rfm.py
python 04_viz.py
```

## 文件结构

```
01_eda.py            数据体检
02_check.py          问题诊断（分组对照验证）
03_clean.py          数据清洗
04_rfm.py            RFM 三指标 + 八分层
04_viz.py            可视化（月度趋势/分层/国家）
figures/             图表输出
m01_data_dictionary.md   数据字典
m02_cleaning_log.md      清洗规则与执行记录
m03_rfm_notes.md         RFM 结果与业务建议
```

## 未来工作

- 复购与留存分析：同期群（Cohort）曲线
- 退货率分析（退货单已单独存 `data/returns.csv`）
- 海外（非英国）市场的独立分层分析
