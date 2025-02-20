import plotly.express as px
import pandas as pd

# Generate some sample data
data = {
    'product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
  'sales': [120, 80, 150, 90, 110],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Toys', 'Clothing'],
    'price': [50, 20, 80, 15, 30]
}
df = pd.DataFrame(data)

# 1. Bar Chart
fig_bar = px.bar(df, x='product', y='sales', title='Product Sales')
# Interaction: Hovering shows product name and sales value

# 2. Histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution of Products')
# Interaction: Hovering shows bin range and frequency

# 3. Pie Chart (similar concept to tree map in showing proportions)
fig_pie = px.pie(df, names='category', values='sales', title='Sales Distribution by Category')
# Interaction: Hovering shows category name and its proportion of sales

# 4. Gauge Chart (simulated using a circular indicator for simplicity)
from plotly.graph_objects import Indicator

fig_gauge = px.Indicator(
    mode="gauge+number",
    value=df['sales'].sum(),
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Total Sales"}
)

# Create a dashboard layout using subplots
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Product Sales", "Price Distribution", "Sales by Category", "Total Sales")
)

fig.add_trace(fig_bar.data[0], row=1, col=1)
fig.add_trace(fig_hist.data[0], row=1, col=2)
fig.add_trace(fig_pie.data[0], row=2, col=1)
fig.add_trace(fig_gauge.data[0], row=2, col=2)

fig.update_layout(height=800, width=1000, title_text="Sample Dashboard")

# Show the dashboard
fig.show()