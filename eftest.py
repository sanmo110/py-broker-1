import efinance as ef
import pprint
import numpy as np
import pandas as pd

quote_ids = ef.futures.get_realtime_quotes()
quote_ids.to_csv('output.csv', index=False)

# 获取期货历史数据
futures_history_data = ef.futures.get_quote_history('8.070130',klt=101)
futures_history_data.to_csv('IH50.csv',index=False)

futures_history_data = ef.futures.get_quote_history('8.040130',klt=101)
futures_history_data.to_csv('IF300.csv',index=False)

futures_history_data = ef.futures.get_quote_history('8.060130',klt=101)
futures_history_data.to_csv('IC500.csv',index=False)

futures_history_data = ef.futures.get_quote_history('8.150130',klt=101)
futures_history_data.to_csv('IM1000.csv',index=False)