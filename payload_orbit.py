import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'Payload': [100, 150, 80, 200, 120, 90, 180, 130, 110, 170],
    'Orbit Type': ['Low Earth Orbit', 'Geostationary Orbit', 'Low Earth Orbit', 'Polar Orbit', 'Geostationary Orbit',
                   'Low Earth Orbit', 'Medium Earth Orbit', 'Polar Orbit', 'Geostationary Orbit', 'Medium Earth Orbit']
}
df = pd.DataFrame(data)

# Map orbit types to numerical values for plotting (since scatter plot works with numbers)
orbit_type_mapping = {orbit: num for num, orbit in enumerate(set(df['Orbit Type']))}
df['Orbit Type Numeric'] = df['Orbit Type'].map(orbit_type_mapping)

# Create the scatter plot
plt.scatter(df['Payload'], df['Orbit Type Numeric'])

# Map the numerical values back to the actual orbit type names for the y-axis labels
plt.yticks(list(orbit_type_mapping.values()), list(orbit_type_mapping.keys()))

plt.xlabel('Payload')
plt.ylabel('Orbit Type')
plt.title('Payload vs. Orbit Type')
plt.show()