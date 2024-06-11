import pandas as pd

# 读取 TSV 文件
file_path = 'large_train/behaviors.tsv'
data = pd.read_csv(file_path, sep='\t', header=None, names=['user_id', 'timestamp', 'clicks', 'products'])

# 转换时间戳为 datetime 格式
data['timestamp'] = pd.to_datetime(data['timestamp'])

# 填充 NaN 值并将所有列转换为字符串类型
data = data.fillna('')
data['clicks'] = data['clicks'].astype(str)
data['products'] = data['products'].astype(str)

# 按用户和时间戳排序
data_sorted = data.sort_values(by=['user_id', 'timestamp'])

# 聚合用户点击序列
user_click_sequences = data_sorted.groupby('user_id').agg({
    # 'timestamp': list,
    'clicks': lambda x: ' '.join(x),
    # 'products': lambda x: ' '.join(x)
}).reset_index()

# 输出清洗后的数据
print(user_click_sequences)

# 保存清洗后的数据到新的 TSV 文件
user_click_sequences.to_csv('cleaned_data.tsv', sep='\t', index=False)
