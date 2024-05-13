# Loads csv file into pandas dataframe then into a SQLite file

import pandas as pd
import sqlite3
import os

def load_csv_file(file_name):
    return pd.read_csv(file_name)

def create_sqlite_database(dataframe, database_name, table_name):
    conn = sqlite3.connect(database_name)
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

script_dir = os.path.dirname(__file__)

csv_file_path = os.path.join(script_dir, "addresses.csv")

df = load_csv_file(csv_file_path)

df.columns = ["First Name", "Last Name", "Address", "City", "State", "Zip"]

print(df)

database_name = "my_database.db"

table_name = "my_table"

create_sqlite_database(df, database_name, table_name)