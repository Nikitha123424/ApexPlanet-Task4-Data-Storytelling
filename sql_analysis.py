import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_excel("Cleaned_Sales_Dataset.xlsx")

# Create SQLite database
connection = sqlite3.connect("sales_database.db")

# Store dataset as a SQL table
df.to_sql("sales", connection, if_exists="replace", index=False)

print("Database and sales table created successfully!")

# SQL Query 7:
# Which category generates the highest sales for each gender?

query = """
SELECT
    Gender,
    Category,
    SUM(Total_Sales) AS Total_Sales
FROM sales
GROUP BY Gender, Category
ORDER BY Gender, Total_Sales DESC;
"""

result = pd.read_sql_query(query, connection)

print("\nSales by Gender and Category:")
print(result)

connection.close()