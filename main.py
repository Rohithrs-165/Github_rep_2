import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(layout="wide")

st.title("E-Commerce Data Analysis")

file_upload=st.file_uploader("Upload the Dataset")
if file_upload is not None:
    df=pd.read_csv(file_upload)
    st.success("File Loaded Successfully")
    st.subheader("Data preview")
    st.dataframe(df.head())
    st.dataframe(df.tail())
    st.subheader("Data Information")
    col1,col2,col3,col4=st.columns(4)
    col1.metric("No.of.Rows",df.shape[0])
    col2.metric("No.of.Columns",df.shape[1])
    col3.metric("No.of Null Values",df.isnull().sum().sum())
    col4.metric("No.of Duplicate Values",df.duplicated().sum())
# Line plot
#Most Sold Products
    st.subheader("Most Sold products")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(data=df,x="Category",color="purple",ax=ax)
    ax.set_title("Products Sold by Category")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
#Total Revenue by Category
    st.subheader("Total Revenue by Category")
    fig,ax = plt.subplots(figsize=(8,5))
    category_sales = df.groupby("Category")["Final_Price(Rs.)"].sum()
    category_sales.plot(kind="bar",color="orange",ax=ax)
    ax.set_ylabel("Revenue")
    ax.set_title("Revenue by Category")
    st.pyplot(fig)
#Boxplot Category vs Price
    st.subheader("Boxplot: Category vs Price")
    fig,ax = plt.subplots(figsize=(8,5))
    sns.boxplot(data=df,x="Category",y="Final_Price(Rs.)",color="red",ax=ax)
    ax.set_title("Price Distribution by Category")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
# Monthly Sales Trend
    st.subheader("Monthly Sales Trend")
    df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"],errors="coerce",dayfirst=True)
    df = df.dropna(subset=["Purchase_Date"])
    df["Month"] = df["Purchase_Date"].dt.to_period("M").astype(str)
    monthly_sales = df.groupby("Month").size()
    fig, ax = plt.subplots(figsize=(8,5))
    monthly_sales.plot(kind="line",marker="o",color="blue",linewidth=2,markersize=8,ax=ax)
    ax.set_title("Monthly Sales Trend", fontsize=14)
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Orders")
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)
#Average discount by category
    st.subheader("Average Discount by Category")
    avg_discount = df.groupby("Category")["Discount (%)"].mean()
    fig, ax = plt.subplots(figsize=(8,5))
    avg_discount.plot(kind="bar",color="green",edgecolor="black",ax=ax)
    ax.set_title("Average Discount by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Average Discount (%)")
    plt.xticks(rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    st.pyplot(fig)
    #To view the full Dataset
    st.subheader("Full Dataset")
    st.dataframe(df)
else:
    st.info("Please upload a CSV file to proceed with the analysis.")