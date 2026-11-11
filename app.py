
import pandas as pd
import streamlit as st

st.title("Cafe Sales Dashboard")

# Load data
df = pd.read_csv("cafe_sales.csv")

# Branch selector
branches = ["All Branches"] + sorted(df["branch"].unique())

selected_branch = st.selectbox("Select Branch", branches)

# Filter data
if selected_branch == "All Branches":
    filtered_df = df
else:
    filtered_df = df[df["branch"] == selected_branch]

# Total revenue
total_revenue = filtered_df["total_sar"].sum()

st.metric("Total Revenue (SAR)", total_revenue)

# Revenue by product
product_revenue = filtered_df.groupby("product")["total_sar"].sum()

st.subheader("Revenue by Product")

st.bar_chart(product_revenue)
