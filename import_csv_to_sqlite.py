import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(r"C:\Users\ConnyMohlin\OneDrive - Digital Media Installer International AB\HTML\Barcode\products.csv")

# Convert the Barcode column to string
df['Barcode'] = df['Barcode'].astype(str)

# Insert the data into the Product table
df.to_sql("Product", conn, if_exists="append", index=False)

# Close the connection
conn.close()
