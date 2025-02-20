import pandas as pd
import matplotlib.pyplot as plt

# 创建示例数据
data = {
    'Flight Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Launch Site': ['Site A', 'Site B', 'Site A', 'Site C', 'Site B', 'Site A', 'Site C', 'Site B', 'Site A', 'Site C']
}
df = pd.DataFrame(data)

# 将发射地点映射为数值以便绘图（因为散点图处理的是数值数据）
launch_site_mapping = {site: num for num, site in enumerate(set(df['Launch Site']))}
df['Launch Site Numeric'] = df['Launch Site'].map(launch_site_mapping)

# 创建散点图
plt.scatter(df['Flight Number'], df['Launch Site Numeric'])

# 将数值重新映射回实际的发射地点名称，用于y轴标签
plt.yticks(list(launch_site_mapping.values()), list(launch_site_mapping.keys()))

plt.xlabel('Flight Number')
plt.ylabel('Launch Site')
plt.title('Flight Number vs. Launch Site')
plt.show()