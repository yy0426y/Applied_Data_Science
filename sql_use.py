import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests  # Used for simulating data retrieval from the web

# 1. Data Collection: Simulate retrieving data from the web (can be replaced with data from files, databases, etc. in practice)
url = "https://example.com/fake_sales_data"  # This is a simulated URL
response = requests.get(url)
# Assume the returned data is in JSON format and convert it to a DataFrame
data = pd.DataFrame(response.json())

# 2. Data Cleaning
# Handle missing values. Fill missing values in numeric columns with the mean of that column,
# and fill missing values in string columns with 'unknown'
for col in data.columns:
    if data[col].dtype in ['int64', 'float64']:
        data[col] = data[col].fillna(data[col].mean())
    elif data[col].dtype == 'object':
        data[col] = data[col].fillna('unknown')

# Remove duplicate rows
data = data.drop_duplicates()

# 3. Data Transformation
# Standardize a numeric column (using Z-score normalization)
def z_score_normalize(x):
    return (x - np.mean(x)) / np.std(x)

data['sales_amount'] = z_score_normalize(data['sales_amount'])

# Convert the date column to datetime type
data['date'] = pd.to_datetime(data['date'])

# 4. Data Analysis
# Calculate the average sales amount for each product in each month (similar to SQL's GROUP BY and aggregation operation)
data['month'] = data['date'].dt.month
average_sales_per_month_product = data.groupby(['month', 'product_name'])['sales_amount'].mean().reset_index()

# 5. Data Visualization
# Draw a bar chart to show the average sales amount of different products in each month
import seaborn as sns

sns.barplot(x='month', y='sales_amount', hue='product_name', data=average_sales_per_month_product)
plt.xlabel('Month')
plt.ylabel('Average Sales Amount')
plt.title('Average Sales Amount per Month and Product')
plt.show()