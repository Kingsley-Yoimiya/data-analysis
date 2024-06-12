import pandas as pd

# 读取 CSV 文件，使用逗号作为分隔符
file_path = 'large_train/ijcai2016_taobao.csv'
data = pd.read_csv(file_path, sep=',')

# 确保列名为 ['use_ID', 'sel_ID', 'ite_ID', 'cat_ID', 'act_ID', 'time']
data.columns = ['use_ID', 'sel_ID', 'ite_ID', 'cat_ID', 'act_ID', 'time']

# 转换时间戳为 datetime 格式
data['time'] = pd.to_datetime(data['time'])

# 填充 NaN 值并将所有列转换为字符串类型
data = data.fillna('')
data['use_ID'] = data['use_ID'].astype(str)
data['ite_ID'] = data['ite_ID'].astype(str)

# 按用户和时间戳排序
data = data.sort_values(by=['use_ID', 'time'])

# 聚合用户点击序列
user_click_sequences = data.groupby('use_ID').agg({
    'ite_ID': lambda x: ' '.join(x)
}).reset_index()

# 输出清洗后的数据
print(user_click_sequences)

# 保存清洗后的数据到新的 TSV 文件
user_click_sequences.to_csv('cleaned_data.tsv', sep='\t', index=False)
