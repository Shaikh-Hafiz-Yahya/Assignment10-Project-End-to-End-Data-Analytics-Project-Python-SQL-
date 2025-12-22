# Create a project using the attached link which get the data from Kaggle and then apply trnasformation 
# using pandas and finally load the transform data into Sql Server.

# Please apply 5 analysis after loading the data into Sql Server.

import pandas as pd

# Load dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print("Initial Shape:", df.shape)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Handle missing values
df["postal_code"] = df["postal_code"].fillna(0).astype(int)

# Convert dates
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# Feature Engineering
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["profit_margin"] = (df["profit"] / df["sales"]) * 100

# Remove duplicates
df = df.drop_duplicates()

print("Transformed Shape:", df.shape)
print(df.head())

# Save transformed data
df.to_csv("data/superstore_transformed.csv", index=False)

print("Transformation completed successfully")
