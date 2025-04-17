import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Interactive Data Explorer")

# Sidebar for user input
st.sidebar.header("Customize Your Chart")
num_points = st.sidebar.slider("Number of data points:", 10, 100, 50)
chart_type = st.sidebar.selectbox("Choose chart type:", ["Line", "Scatter"])

# Generate random data
data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=['x', 'y']
)

# Display data table
if st.checkbox("Show raw data"):
    st.write("Raw Data:")
    st.dataframe(data)

# Plot based on chart type
st.write("Your Chart:")
if chart_type == "Line":
    st.line_chart(data)
else:
    fig, ax = plt.subplots()
    ax.scatter(data['x'], data['y'], color='blue')
    st.pyplot(fig)

# Add a button
if st.button("Say Hello"):
    st.write("Hello, Streamlit!")