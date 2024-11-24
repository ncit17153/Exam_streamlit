# Save this as `app.py` in your GitHub repository

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
filename = "https://raw.githubusercontent.com/ncit17153/Exam_streamlit/refs/heads/main/Automobile.csv"
headers = [
    "symboling", "normalized-losses", "make", "fuel-type", "aspiration",
    "num-of-doors", "body-style", "drive-wheels", "engine-location",
    "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
    "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
    "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"
]
df = pd.read_csv(filename, names=headers)

# Title of the app
st.title("Automobile Data Analysis")

# Show the dataframe
if st.checkbox("Show Raw Data"):
    st.write(df)

# Handle missing values
df.replace("?", pd.NA, inplace=True)
numeric_columns = ["normalized-losses", "bore", "stroke", "horsepower", "peak-rpm", "price"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric
    df[col] = df[col].fillna(df[col].mean())  # Assign back after filling NaN

categorical_columns = ["num-of-doors"]
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Calculate the mean value for the "normalized-losses" column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
st.write(f"Average of normalized-losses: {avg_norm_loss:.2f}")

# Visualization 1: Distribution of car prices
st.subheader("Distribution of Car Prices")
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
st.pyplot()

# Average price by body style and fuel type
st.subheader("Average Price by Body Style and Fuel Type")
pivot = df.pivot_table(values='price', index='body-style', columns='fuel-type', aggfunc='mean')
sns.heatmap(pivot, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Average Price by Body Style and Fuel Type')
st.pyplot()

# Visualization 2: Scatter plot of horsepower vs. price
st.subheader("Horsepower vs. Price")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='horsepower', y='price', data=df, color='red')
plt.title('Horsepower vs. Price')
plt.xlabel('Horsepower')
plt.ylabel('Price')
st.pyplot()

# Visualization 3: Count of cars by fuel type
st.subheader("Count of Cars by Fuel Type")
plt.figure(figsize=(6, 4))
sns.countplot(x='fuel-type', data=df, palette='Set2')
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
st.pyplot()

# Visualization 4: Price distribution by body style
st.subheader("Price Distribution by Body Style")
plt.figure(figsize=(8, 5))
sns.boxplot(x='body-style', y='price', data=df, palette='Set3')
plt.title('Price Distribution by Body Style')
plt.xlabel('Body Style')
plt.ylabel('Price')
st.pyplot()

# Check if there are any NaN values in each column
st.subheader("Missing Data Check")
missing_data = df.isnull().sum()
st.write(missing_data)

# Optionally add more interactive widgets here as needed
