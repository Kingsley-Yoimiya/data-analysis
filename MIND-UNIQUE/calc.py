import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# 读取清洗后的数据
file_path = 'cleaned_data.tsv'
cleaned_data = pd.read_csv(file_path, sep='\t')

user_count = cleaned_data['user_id'].nunique()
print(f'用户数量: {user_count}')

# 填充 NaN 值并将所有列转换为字符串类型
cleaned_data = cleaned_data.fillna('')
cleaned_data['clicks'] = cleaned_data['clicks'].astype(str)

# 将点击序列转换为列表
cleaned_data['clicks'] = cleaned_data['clicks'].apply(lambda x: x.split())

def calculate_unique_token_ratio(cleaned_data, B, D):
    # 随机选择 B 个用户
    selected_users = cleaned_data.sample(n=B, random_state=42)
    
    token_num = 0
    unique_tokens = set()
    
    for _, row in selected_users.iterrows():
        # 获取用户最新的 D 条点击
        clicks = row['clicks'][-D:]
        token_num += len(clicks)
        unique_tokens.update(clicks)
    
    unique_token_num = len(unique_tokens)
    if token_num == 0:
        return 0
    return unique_token_num / token_num

# 参数 B 和 D 的范围
B_values = range(250, 20000, 4000)  # 1, 6, 11, 16
D_values = range(10, 200, 20)  # 1, 3, 5, 7, 9

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

# 转换为 DataFrame
results_df = pd.DataFrame(results, columns=['B', 'D', 'Ratio'])

# 绘图
fig, ax = plt.subplots()
for B in B_values:
    subset = results_df[results_df['B'] == B]
    ax.plot(subset['D'], subset['Ratio'], marker='o', label=f'B={B}')

ax.set_xlabel('D')
ax.set_ylabel('Unique Token Ratio')
ax.set_title('Unique Token Ratio vs. D for Different B')
ax.legend()

fig.savefig('unique_token_ratio.svg', format='svg')

# plt.show()

