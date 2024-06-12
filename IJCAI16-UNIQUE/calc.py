import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import pickle

def calculate_unique_token_ratio(cleaned_data, B, D):
    # 随机选择 B 个用户
    selected_users = cleaned_data.sample(n=B, random_state=42)
    
    token_num = 0
    unique_tokens = set()
    
    for _, row in selected_users.iterrows():
        # 获取用户最新的 D 条点击
        clicks = row['ite_ID'][-D:]
        token_num += len(clicks)
        unique_tokens.update(clicks)
    
    unique_token_num = len(unique_tokens)
    if token_num == 0:
        return 0
    return unique_token_num / token_num

# 参数 B 和 D 的范围
B_values = range(250, 22000, 4000)
D_values = range(10, 201, 10)

# 结果缓存文件路径
cache_file = 'results_cache.pkl'

# 检查是否存在缓存文件
if os.path.exists(cache_file):
    with open(cache_file, 'rb') as f:
        results = pickle.load(f)
else:
    # 读取清洗后的数据
    file_path = 'cleaned_data.tsv'
    cleaned_data = pd.read_csv(file_path, sep='\t')

    user_count = cleaned_data['use_ID'].nunique()
    print(f'用户数量: {user_count}')

    # 填充 NaN 值并将所有列转换为字符串类型
    cleaned_data = cleaned_data.fillna('')
    cleaned_data['ite_ID'] = cleaned_data['ite_ID'].astype(str)

    # 将点击序列转换为列表
    cleaned_data['ite_ID'] = cleaned_data['ite_ID'].apply(lambda x: x.split())
    results = []
    # 计算并存储结果
    for B in B_values:
        for D in D_values:
            ratios = []
            for _ in range(5):
                ratios.append(calculate_unique_token_ratio(cleaned_data, B, D))
            ratio = np.mean(ratios)
            results.append((B, D, ratio))
            print(B, D, ratio)
    # 保存结果到缓存文件
    with open(cache_file, 'wb') as f:
        pickle.dump(results, f)

# 转换为 DataFrame
results_df = pd.DataFrame(results, columns=['B', 'D', 'Ratio'])

# 绘图
fig, ax = plt.subplots(figsize=(12, 8))

# 调整主图和放大图的布局
# fig.subplots_adjust(left=0.1, right=0.75)

# 主图使用正常刻度
for B in B_values:
    subset = results_df[results_df['B'] == B]
    ax.plot(subset['D'], subset['Ratio'], marker='o', label=f'B={B}')

ax.set_xlabel('D')
ax.set_ylabel('Unique Token Ratio')
ax.set_title('Unique Token Ratio vs. D for Different B')
ax.legend(loc='upper right')

fig.savefig('unique_token_ratio.svg', format='svg')

plt.show()
