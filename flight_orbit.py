import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Flight Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Orbit Type': ['Low Earth Orbit', 'Geostationary Orbit', 'Low Earth Orbit', 'Polar Orbit', 'Geostationary Orbit',
                   'Low Earth Orbit', 'Medium Earth Orbit', 'Polar Orbit', 'Geostationary Orbit', 'Medium Earth Orbit']
}
df = pd.DataFrame(data)

# Create the scatter plot using seaborn
sns.scatterplot(x='Flight Number', y='Orbit Type', data=df)

plt.xlabel('Flight Number')
plt.ylabel('Orbit Type')
plt.title('Flight Number vs. Orbit Type')
plt.show()