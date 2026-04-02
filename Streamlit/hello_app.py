import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Dashboard Title")
st.header("Section Header")
st.subheader("Subsection")
st.text("Fixed-width plain text")
st.caption("Small grey caption text")
st.markdown("**Bold**, *Italics*, and `code` using standard Markdown syntax")
st.markdown("---")
st.code("""
def hello():
        return "This renders as a code block with syntax highlighting"   
""", language="python")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Left Column")
    st.write("Any content placed inside this block appears on the left")
    st.metric(label="Total Sales", value= "₹48,000", delta="+12%")

with col2:
    st.subheader("Right Column")
    st.write("This content appears on the right, at the same vertical level")
    st.metric(label="Active Users", value= "1,284", delta="-3%")

df = sns.load_dataset("tips")
st.subheader("Method 1: st.write()")
st.write(df.head(5))

st.subheader("Method 2: st.dataframe() - Interactive Table")
st.dataframe(df.head(30), use_container_width=True)

st.subheader("Method 3: st.table() - Static Table")
st.table(df.groupby("day")["total_bill"].mean().round(2))

st.subheader("Bill Distribution by Day")
fig, ax = plt.subplots(figsize = (8, 4))
sns.boxplot(data=df, x="day", y="total_bill", ax=ax, palette="muted")
ax.set_xlabel("Day of Week")
ax.set_ylabel("Total Bill (₹)")
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)