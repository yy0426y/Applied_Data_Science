import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Orbit Type': ['Low Earth Orbit', 'Geostationary Orbit', 'Polar Orbit', 'Medium Earth Orbit'],
    'Successful Launches': [80, 60, 40, 70],
    'Total Launches': [100, 80, 50, 90]
}
df = pd.DataFrame(data)

# Calculate the success rate for each orbit type
df['Success Rate'] = df['Successful Launches'] / df['Total Launches'] * 100

# Create the bar chart
plt.bar(df['Orbit Type'], df['Success Rate'])

plt.xlabel('Orbit Type')
plt.ylabel('Success Rate (%)')
plt.title('Success Rate vs. Orbit Type')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()