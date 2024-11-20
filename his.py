import copy
import matplotlib.pyplot as plt
import pandas as pd

# 给matplotlib指定中文字体
plt.rcParams['font.family'] = 'SimHei'
# 正常显示坐标轴负号
plt.rcParams['axes.unicode_minus'] = False


# 渲染直方图
def render_hist(name, ori_data, bins=200):
    # 创建一个示例 DataFrame
    print("-------", )
    print(name)
    print("-------", )
    data = {'Value': ori_data}
    df = pd.DataFrame(data)
    mean = df['Value'].mean()
    std = df['Value'].std()
    print("均值：", mean)
    print("标准差：", std)
    min_value = df['Value'].min()
    max_value = df['Value'].max()
    print("最小值：", min_value)
    print("最大值：", max_value)
    median = df['Value'].median()
    print("中位数：", median)

    str = ''
    for i in range(1, 10):
        rate = i / 10
        q = round(df['Value'].quantile(rate), 3)
        p_str = f"{rate} {q}"
        print(f"分位数：{p_str}")
        str = str + p_str + '\n'

    # 绘制直方图
    df['Value'].hist(bins=bins)
    # 设置标题和坐标轴标签
    plt.title(name)
    plt.xlabel('幅度')
    plt.ylabel('频次')
    plt.text(0, 0, str, fontsize=12, color='red', fontweight='bold')
    # 显示图形
    plt.show()
    print("================================")
    print("\n")



def duplicate_first_element(s):
    """
    将输入的Series的第一个元素复制一份并放到Series的第一个位置，返回调整后的新Series。

    参数:
    s (pd.Series): 输入的Series对象

    返回:
    pd.Series: 调整后的新Series对象
    """
    first_value = s.iloc[0]  # 获取第一个元素的值
    new_index = list(s.index)
    new_index.insert(0, s.index[0])  # 将原索引的第一个元素再次插入到第一个位置
    new_index.pop(-1)  # 去掉新索引列表的最后一个元素，对应去掉原Series的最后一个元素
    new_s = pd.Series(s.values, index=new_index)  # 根据调整后的索引重新构建Series
    return new_s


# 开盘,收盘,最高,最低,成交量,成交额,振幅,涨跌幅,涨跌额,换手率
def get_calc_day_up_down_rate_data(file, col_name='涨跌幅'):
    data = pd.read_csv(file)
    data_updown_rate_ori = data[col_name]
    data_updown_rate = copy.deepcopy(data_updown_rate_ori)
    for i in range(len(data_updown_rate)):
        data_updown_rate[i] = data_updown_rate_ori[i]
    return data_updown_rate


def get_calc_day_max_down_rate_data(file, col_name_down='最低', col_name='收盘'):
    data = pd.read_csv(file)
    data_down_ori = data[col_name_down]
    data_end_ori = data[col_name]
    data_updown_rate = copy.deepcopy(data_end_ori)
    data_updown_rate = duplicate_first_element(data_updown_rate)
    for i in range(len(data_updown_rate)):
        data_updown_rate[i] = (data_down_ori[i] - data_end_ori[i]) / data_end_ori[i] * 100
    return data_updown_rate


def get_calc_day_max_up_down_rate_data(file, col_name_down='最低', col_name_up='最高',
                                       col_name='收盘'):
    data = pd.read_csv(file)
    data_down_ori = data[col_name_down]
    data_up_ori = data[col_name_up]
    data_end_ori = data[col_name]
    data_updown_rate = copy.deepcopy(data_end_ori)
    data_updown_rate = duplicate_first_element(data_updown_rate)
    for i in range(len(data_updown_rate)):
        data_updown_rate[i] = (data_up_ori[i] - data_down_ori[i]) / data_end_ori[i] * 100
    return data_updown_rate


def get_calc_day_max_up_rate_data(file, col_name_up='最高', col_name='收盘'):
    data = pd.read_csv(file)
    data_up_ori = data[col_name_up]
    data_end_ori = data[col_name]
    data_updown_rate = copy.deepcopy(data_end_ori)
    data_updown_rate = duplicate_first_element(data_updown_rate)
    for i in range(len(data_updown_rate)):
        data_updown_rate[i] = (data_up_ori[i] - data_end_ori[i]) / data_end_ori[i] * 100
    return data_updown_rate


def get_calc_day_open_max_down_rate_data(file, col_name_down='最低', col_name='开盘'):
    data = pd.read_csv(file)
    data_down_ori = data[col_name_down]
    data_end_ori = data[col_name]
    data_updown_rate = copy.deepcopy(data_end_ori)
    for i in range(len(data_updown_rate)):
        data_updown_rate[i] = (data_down_ori[i] - data_end_ori[i]) / data_end_ori[i] * 100
    return data_updown_rate


def get_calc_day_open_max_up_rate_data(file, col_name_up='最高', col_name='开盘'):
    data = pd.read_csv(file)
    data_up_ori = data[col_name_up]
    data_end_ori = data[col_name]
    data_updown_rate = copy.deepcopy(data_end_ori)
    for i in range(len(data_updown_rate)):
        data_updown_rate[i] = (data_up_ori[i] - data_end_ori[i]) / data_end_ori[i] * 100
    return data_updown_rate


def render_file(title, file):
    render_hist(title + '-日内涨跌幅', get_calc_day_up_down_rate_data(file))
    render_hist(title + '-日内波动幅度', get_calc_day_max_up_down_rate_data(file))
    render_hist(title + '-日内低点跌幅', get_calc_day_max_down_rate_data(file))
    render_hist(title + '-日内高点涨幅', get_calc_day_max_up_rate_data(file))
    render_hist(title + '-相对开盘日内低点跌幅', get_calc_day_open_max_down_rate_data(file))
    render_hist(title + '-相对开盘日内高点涨幅', get_calc_day_open_max_up_rate_data(file))


render_file('IH50-15年至今', 'IH50.csv')
render_file('IF300-15年至今', 'IF300.csv')
render_file('IC500-15年至今', 'IC500.csv')
render_file('IM1000-15年至今', 'IM1000.csv')
