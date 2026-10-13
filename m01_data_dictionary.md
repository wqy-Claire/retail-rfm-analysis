InvoiceNo 订单号（C 开头=退货）、StockCode 商品编码、Description 商品名、Quantity 数量（负=退货）、InvoiceDate 下单时间、UnitPrice 单价、CustomerID 客户ID（有缺失）、Country 国家

raw_data(1067371, 8)

df类型
Invoice            str 
StockCode          str
Description        str Y
Quantity         int64 Y
InvoiceDate        str ？
Price          float64 Y
Customer ID    float64 
Country            str 

df空缺值个数
Invoice             0
StockCode           0
Description      4382
Quantity            0
InvoiceDate         0
Price               0
Customer ID    243007
Country             0

df重复行数
34335

df的描述
           Quantity         Price    Customer ID
count  1.067371e+06  1.067371e+06  824364.000000
mean   9.938898e+00  4.649388e+00   15324.638504
std    1.727058e+02  1.235531e+02    1697.464450
min   -8.099500e+04 -5.359436e+04   12346.000000
25%    1.000000e+00  1.250000e+00   13975.000000
50%    3.000000e+00  2.100000e+00   15255.000000
75%    1.000000e+01  4.150000e+00   16797.000000
max    8.099500e+04  3.897000e+04   18287.000000