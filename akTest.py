import akshare as ak

# 获取中证 500 指数历史数据
df = ak.stock_zh_index_hist_csindex(symbol="000905", start_date="20220101", end_date="20241119")
print(df)