# Python implementation to create a Database in MySQL
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


class DatabaseConnector:
    """
    Class responsible for creating a database on a MySQL server.
    """
    def __init__(self):
        """
        Initialize the DatabaseCreator with the given MySQL credentials.
        
        Args:
            host (str): The hostname or IP address of the MySQL server.
            user (str): The MySQL username.
            password (str): The MySQL user's password.
        """
        load_dotenv()

        # Retrieve credentials from environment variables
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.database = os.getenv('DB_NAME')

    def connect(self):
        """
        Establishes a connection to the MySQL server. 
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def close(self):
        """
        Closes the database connection if it is open.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("MySQL connection closed.")


class DatabaseCreator(DatabaseConnector):

    def create_database(self, database_name):
        """
        Creates the specified database if it does not already exist.

        Args:
            database_name (str): The name of the database to create.
        """
        if not self.connection:
            print("No active connection. Call connect() first.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`")
            print(f"Database '{database_name}' created or already exists.")
        except Error as e:
            print(f"Error creating database: {e}")