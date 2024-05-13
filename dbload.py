# Loads db file into a pandas dataframe then displays

import pandas as pd
import sqlite3


def load_sqlite_data(database_name, table_name):
    conn = sqlite3.connect(database_name)
    query = "SELECT * FROM {}".format(table_name)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

database_name = "my_database.db"

table_name = "my_table"

df_from_db = load_sqlite_data(database_name, table_name)

print(df_from_db)