import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def init():
    try:
        connection = psycopg2.connect(
        database="postgres",
        user="username",
        password="password",
        host="127.0.0.1",
        port="5432"
    )

        cursor = connection.cursor()

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS main (
        id SERIAL PRIMARY KEY,
        url VARCHAR(100),
        image_value INT,
        text_value INT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(create_table_sql)

        # Commit the transaction
        connection.commit()

        print("Table Main Created")
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

if __name__ == "__main__":
    save_url_to_db("https://catipowero.com")