import mysql.connector
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

def delete_database():
    connection = None
    cursor = None
    try:
        # Get MySQL credentials from environment variables
        mysql_user = os.getenv("MYSQL_USER")
        mysql_password = os.getenv("MYSQL_PASSWORD")

        if not mysql_user or not mysql_password:
            print("Error: MySQL credentials are not set in environment variables.")
            return


        # Connect to the MySQL server using credentials from environment variables
        connection = mysql.connector.connect(
                host="localhost", # MySQL server hosthame
                user=mysql_user,
                password=mysql_password,
                auth_plugin="mysql_native_password"
            )

        # Create a cursor object
        cursor = connection.cursor()

        # SQL statement to drop the database if it exists
        cursor.execute("DROP DATABASE IF EXISTS hbtn_0c_0")

        print("Database deleted successfully, if it existed.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up and close the cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    delete_database()
