import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Payload': [100, 150, 80, 200, 120, 90, 180, 130, 110, 170],
    'Launch Site': ['Site A', 'Site B', 'Site A', 'Site C', 'Site B', 'Site A', 'Site C', 'Site B', 'Site A', 'Site C']
}
df = pd.DataFrame(data)

# Map launch sites to numerical values for plotting (since scatter plot works with numbers)
launch_site_mapping = {site: num for num, site in enumerate(set(df['Launch Site']))}
df['Launch Site Numeric'] = df['Launch Site'].map(launch_site_mapping)

# Create the scatter plot
plt.scatter(df['Payload'], df['Launch Site Numeric'])

# Map the numerical values back to the actual launch site names for the y-axis labels
plt.yticks(list(launch_site_mapping.values()), list(launch_site_mapping.keys()))

plt.xlabel('Payload')
plt.ylabel('Launch Site')
plt.title('Payload vs. Launch Site')
plt.show()