import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")
df["revenue"] = df["price"] * df["quantity"]

st.title("Restaurant Sales Dashboard")

# Total revenue
st.metric("Total Revenue", f"${df['revenue'].sum():,.2f}")

# Revenue by item
item_revenue = df.groupby("item")["revenue"].sum()
st.subheader("Revenue by Item")
st.bar_chart(item_revenue)

# Daily revenue
daily_revenue = df.groupby("date")["revenue"].sum()
st.subheader("Daily Revenue Trend")
st.line_chart(daily_revenue)
