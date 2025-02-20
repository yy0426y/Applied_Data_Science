import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Data Collection: Read data from a CSV file
# Assume the data file is named'sales_data.csv'
data = pd.read_csv('sales_data.csv')

# 2. Data Cleaning
# Handle missing values, simply drop rows with missing values here
data = data.dropna()

# Check and handle duplicate values
data = data.drop_duplicates()

# 3. Data Transformation
# Convert the 'date' column to datetime type
data['date'] = pd.to_datetime(data['date'])

# Normalize the numerical column'sales_amount'
# The formula: (x - min(x)) / (max(x) - min(x))
data['sales_amount'] = (data['sales_amount'] - data['sales_amount'].min()) / (
        data['sales_amount'].max() - data['sales_amount'].min())

# 4. Data Analysis
# Calculate the average sales amount for each product
# Group the data by 'product_name' and calculate the mean of'sales_amount'
average_sales_per_product = data.groupby('product_name')['sales_amount'].mean()

# 5. Data Visualization
# Plot a bar chart to show the average sales amount for each product
average_sales_per_product.plot(kind='bar')
plt.xlabel('Product Name')
plt.ylabel('Average Sales Amount')
plt.title('Average Sales Amount per Product')
plt.show()