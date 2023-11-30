import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd
import streamlit as st
from config import DB_HOST, DB_PORT, DB_NAME, DB_PASSWORD, DB_USER

def init():
    try:
        connection = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

        cursor = connection.cursor()

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS main (
        id SERIAL PRIMARY KEY,
        url VARCHAR(1000),
        image_value FLOAT,
        text_value FLOAT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(create_table_sql)

        # Commit the transaction
        connection.commit()

        return connection
    except Exception as e:
        print(f"error : {str(e)}")



def save_url_to_db(url):
    insert_data_sql = """
    INSERT INTO main (url, image_value, text_value)
    VALUES (%s, %s, %s);
    """

    data_to_insert = (url, 0,0)

    connection  = init()
    try:
        cursor = connection.cursor()

        # Execute the SQL command to insert data
        cursor.execute(insert_data_sql, data_to_insert)

        connection.commit()
        print("Data inserted to DB successfully")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

    finally:
            cursor.close()
            connection.close()

def get_from_db_all_values():
    """
    Fetch all values from a specified table in a SQLite database and display them in a table format.

    Parameters:
    - db_path (str): Path to the SQLite database file.
    - table_name (str): Name of the table to fetch values from.

    Returns:
    - pd.DataFrame: A Pandas DataFrame containing all the values from the specified table.
    """

    # Connect to the SQLite database
    connection = init()

    # Query to fetch all values from the specified table
    query = f"SELECT * FROM main;"

    # Execute the query and fetch the results
    result = pd.read_sql_query(query, connection)

    # Close the database connection
    connection.close()

    return result
     
def update_db(site, score, column):
    connection = init()
    try:
        cursor = connection.cursor()
        query = f"UPDATE main SET {column} = {score} WHERE url = '{site}';"
        cursor.execute(query)
        connection.commit()
        print("Data updated to DB successfully")
    except Exception as e:
        print(f"Error updating data: {str(e)}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    save_url_to_db("https://catipowero.com")