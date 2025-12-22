import pandas as pd
from sqlalchemy import create_engine

# Load transformed data
df = pd.read_csv("data/superstore_transformed.csv")

# SQL Server connection
engine = create_engine(
    "mssql+pyodbc://localhost/SalesDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# Load data
df.to_sql(
    "superstore_sales",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded into SQL Server successfully")
