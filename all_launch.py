import pandas as pd

# Read the data from the CSV file. Replace 'launch_data.csv' with the actual file path if needed.
df = pd.read_csv('launch_data.csv')

# Find the unique launch site names
unique_launch_sites = df['Launch Site'].unique()

print(unique_launch_sites)

launch_sites_list = ['Site A', 'Site B', 'Site A', 'Site C', 'Site B']
df = pd.DataFrame({'Launch Site': launch_sites_list})
unique_launch_sites = df['Launch Site'].unique()
print(unique_launch_sites)