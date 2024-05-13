import pandas as pd
import sqlite3

# Function to load data from SQLite database into a pandas DataFrame
def load_sqlite_data(database_name, table_name):
    conn = sqlite3.connect(database_name)
    query = "SELECT * FROM {}".format(table_name)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Database file name
database_name = "my_database.db"

# Table name
table_name = "my_table"

# Load data from SQLite database into a pandas DataFrame
df_from_db = load_sqlite_data(database_name, table_name)

# Print the DataFrame
print(df_from_db)