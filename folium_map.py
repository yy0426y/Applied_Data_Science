import folium

# Create a base map centered around a specific location (latitude, longitude)
# Here we use the coordinates of a sample location (you can change it as needed)
m = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

# 1. Add a marker
# Let's add a marker at a specific point of interest
marker_location = [37.7765, -122.4230]
folium.Marker(
    location=marker_location,
    popup="This is a sample point of interest",
    icon=folium.Icon(color='blue')
).add_to(m)

# 2. Add a circle
# Suppose we want to represent an area around a location with a circle
circle_location = [37.7750, -122.4200]
folium.Circle(
    location=circle_location,
    radius=500,  # Radius in meters
    color='red',
    fill=True,
    fill_color='red',
    fill_opacity=0.3,
    popup="This circle represents an area of interest"
).add_to(m)

# 3. Add a line
# Let's create a line to represent a connection between two points
start_point = [37.7730, -122.4210]
end_point = [37.7780, -122.4180]
folium.PolyLine(
    locations=[start_point, end_point],
    color='green',
    weight=2.5,
    opacity=1
).add_to(m)

# Save the map as an HTML file
m.save('example_folium_map.html')