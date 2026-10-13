# 清洗日志 cleaning_log
## Step 0 — 问题清单
1.InvoiceDate为str类型 ｜ 应该转成datetime类型
2.Customer ID为float64 | 应该转成字符串或者类别类型
3.Customer ID和description分别缺失243007行和4382行 ｜ 影响用户分层
4.Quantity, Price min分别为-8，-5 ｜不合理
5.完全重复行34335 ｜ 重复录入需要剔除
6.C开头退货单数量 ｜ 等待统计

## Step 1 — 清洗结果
| 步骤 | 处理行数 | 清洗后剩余行数 |
