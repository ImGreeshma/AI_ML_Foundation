import streamlit as st
import pandas as pd
import seaborn as sns

user_name = st.text_input("Enter Your Name")
st.write(f"Hello {user_name}!")

df = sns.load_dataset("tips")

search_term = st.text_input("Search by Day (Sun, Sat, Fri, Thur):", value="Sun")

min_bill = st.number_input(
    "Minimum Bill Amount (₹):",
    min_value=0.0,
    max_value=float(df["total_bill"].max()),
    value=10.0,
    step=1.0
)

meal_time = st.selectbox(
    "Filter by Meal Time:",
    options=["All", "Lunch", "Dinner"]
)

day_selected = st.multiselect(
    "Select Days to Include:",
    options= df["day"].unique().tolist(),
    default= df["day"].unique().tolist()
)

tip_range = st.slider(
    "Filter by Tip Amount (₹):",
    min_value=float(df["tip"].min()),
    max_value=float(df["tip"].max()),
    value=(1.0, 8.0)
)

filtered = df[
    (df["total_bill"] >= min_bill) &
    (df["day"].isin(day_selected)) &
    (df["tip"] >= tip_range[0]) &
    (df["tip"] <= tip_range[1])
]

show_raw_data = st.checkbox("Show raw data table", value=False)

if show_raw_data :
    st.dataframe(df)

chart_type = st.radio(
    "Choose Chart Type:",
    options=["Bar Chart", "Box Plot", "Scatter Plot"],
    horizontal=True
)
st.write(f"You Selected: {chart_type}")

if meal_time != "All":
    filtered = filtered[filtered["time"] == "meal_time"]

st.subheader(f"Filtered Results: {len(filtered)} rows")
st.dataframe(filtered, use_container_width=True)

st.subheader("Generate Report")
if st.button("Run Analysis"):
    st.success("Analysis Completed")

    col1, col2 = st.columns(2)
    col1.metric("Average Bill", f"(₹){df["total_bill"].mean():.2f}")
    col2.metric("Average Tip", f"(₹){df["tip"].mean():.2f}")
    st.dataframe(df.describe().round(2), use_container_width=True)

st.sidebar.title("Filters")
st.sidebar.markdown("---")

day_filter = st.sidebar.multiselect(
    "Day of Week:",
    options=df["day"].unique().tolist(),
    default=df["day"].unique().tolist()
)

time_filter = st.sidebar.radio(
    "Meal Time:",
    options=["All", "Lunch", "Dinner"]
)

bill_min, bill_max = st.sidebar.slider(
    "Bill Range (₹):",
    min_value = float(df["total_bill"].min()),
    max_value = float(df["total_bill"].max()),
    value=(3.0, 50.0)
)

st.title("Restaurant Tips Dashboard")
filtered = df[
    (df["day"].isin(day_filter)) &
    (df["total_bill"].between(bill_min, bill_max))
]

if time_filter != "All":
    filtered = filtered[filtered["time"] == time_filter]

col1, col2 = st.columns(2)
col1.metric("Records Shown", len(filtered))
col2.metric("Average Tip", f"₹ {filtered["tip"].mean():.2f}" if len(filtered) > 0 else "N/A")
st.dataframe(filtered, use_container_width=True)