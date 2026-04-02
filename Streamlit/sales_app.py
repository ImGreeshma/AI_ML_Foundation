import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Sales Application")
st.subheader("A dashboard for sales")

sales_data = {
    "product" : ['Mobile Phone', 'Dining Table', 'Television', 'Flower Vase', 'Saree', 'Salwar'],
    "category" : ['Electronics', 'Furniture', 'Electronics', 'Home Decor', 'Clothing', 'Clothing'],
    "sales": [35000, 100000, 25000, 1000, 50000, 80000]
}

df = pd.DataFrame(sales_data)

st.sidebar.title("Filters")
st.sidebar.markdown("___")

category = st.sidebar.selectbox(
    "Filter by Category:",
    options=["Electronics", "Furniture", "Home Decor", "Clothing"]
)

filtered = df[df["category"] == category]
st.dataframe(filtered, use_container_width=True)

st.subheader("\n Line Chart for Products Vs Sales")
filtered = filtered.set_index("product")
st.line_chart(filtered["sales"])

