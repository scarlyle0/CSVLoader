import pandas as pd
import sqlite3
import os

def load_csv_file(file_name):
    return pd.read_csv(file_name, encoding='latin1', low_memory=False)  # Specify encoding as latin1 and dtype for specific columns

def create_sqlite_database(dataframe, database_name, table_name):
    conn = sqlite3.connect(database_name)
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)  # Use replace mode
    conn.close()

script_dir = os.path.dirname(__file__)

# Folder containing CSV files
folder_path = os.path.join(script_dir, "csv")

# Database configuration
database_name = "sfdc.db"

# Iterate through CSV files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        print(f"Processing {file_name}...")
        csv_file_path = os.path.join(folder_path, file_name)
        table_name = os.path.splitext(file_name)[0]  # Use file name as table name
        df = load_csv_file(csv_file_path)
        create_sqlite_database(df, database_name, table_name)

print("All CSV files loaded into the database.")