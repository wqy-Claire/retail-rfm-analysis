# 数据字典 Data Dictionary

数据集：Online Retail II（UCI / Kaggle 公开数据集，英国一家注册礼品批发商 2009-12 ~ 2011-12 的真实交易流水）
原始文件：`data/online_retail_II.csv`，1,067,371 行 × 8 列

## 字段说明

| 字段 | 含义 | 类型 | 缺失 | 备注 |
|---|---|---|---|---|
| Invoice | 订单号 | str | 0 | **C 开头 = 退货单**（全表 19,494 行） |
| StockCode | 商品编码 | str | 0 | 如 85123A；部分为非商品编码（运费、坏账等） |
| Description | 商品名称 | str | 4,382 | 缺失行的 Customer ID **100% 也缺失** |
| Quantity | 购买数量 | int64 | 0 | 负值 = 退货/冲销（min -80,950） |
| InvoiceDate | 下单时间 | str（应转 datetime） | 0 | 格式 2009-12-01 07:45:00 |
| Price | 单价（英镑） | float64 | 0 | ≤0 的为赠品/冲销（min -53,594） |
| Customer ID | 客户编号 | float64（应转 str） | 243,007 | 缺失则无法定位用户，RFM 必须删除 |
| Country | 国家/地区 | str | 0 | 共 43 个，绝大多数为 United Kingdom |

## 体检摘要（详见 m02_cleaning_log.md）

- 完全重复行：34,335
- 时间跨度：2009-12-01 ~ 2011-12-09（RFM 快照日建议取 2011-12-10）
- 极端值：Quantity max 80,950、Price max 38,970 —— 批发大单，暂保留
