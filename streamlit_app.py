
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data from GitHub
url = 'https://raw.githubusercontent.com/ncit17153/Exam_streamlit/refs/heads/main/Automobile.csv'
df = pd.read_csv(url)

# Display the title of the app
st.title('Automobile Data Analysis')

# Display the dataset
st.subheader('Dataset Preview')
st.write(df.head())

# Replace "?" with NaN for better handling
df.replace("?", pd.NA, inplace=True)

# Display data after replacing "?" with NaN
st.subheader('Dataset After Handling Missing Values')
st.write(df.head())

# Check for missing values
missing_values = df.isnull().sum()

# Display missing values
st.subheader('Missing Values in Columns')
st.write(missing_values)

# Fill missing numeric values with the column mean
numeric_columns = ["normalized_losses", "bore", "stroke", "horsepower", "peak_rpm", "price"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric
    df[col] = df[col].fillna(df[col].mean())  # Fill NaN with mean

# Fill missing categorical values with mode
categorical_columns = ["num_of_doors"]
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Display updated missing values count
st.subheader('Missing Values After Imputation')
st.write(df.isnull().sum())

# Calculate the mean value for the "normalized-losses" column
avg_norm_loss = df["normalized_losses"].astype("float").mean(axis=0)
st.subheader('Average of Normalized Losses')
st.write(f"Average of normalized_losses: {avg_norm_loss}")

# Visualization 1: Distribution of car prices
st.subheader('Distribution of Car Prices')
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
st.pyplot(plt)

# Average price by body style and fuel type
pivot = df.pivot_table(values='price', index='body_style', columns='fuel_type', aggfunc='mean')
st.subheader('Average Price by Body Style and Fuel Type')
plt.figure(figsize=(8, 5))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Average Price by Body Style and Fuel Type')
st.pyplot(plt)

# Visualization 2: Scatter plot of horsepower vs. price
st.subheader('Horsepower vs. Price')
plt.figure(figsize=(8, 5))
sns.scatterplot(x='horsepower', y='price', data=df, color='red')
plt.title('Horsepower vs. Price')
plt.xlabel('Horsepower')
plt.ylabel('Price')
st.pyplot(plt)

# Visualization 3: Count of cars by fuel type
st.subheader('Count of Cars by Fuel Type')
plt.figure(figsize=(6, 4))
sns.countplot(x='fuel_type', data=df, palette='Set2')
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
st.pyplot(plt)

# Visualization 4: Price distribution by body style
st.subheader('Price Distribution by Body Style')
plt.figure(figsize=(8, 5))
sns.boxplot(x='body_style', y='price', data=df, palette='Set3')
plt.title('Price Distribution by Body Style')
plt.xlabel('Body Style')
plt.ylabel('Price')
st.pyplot(plt)

