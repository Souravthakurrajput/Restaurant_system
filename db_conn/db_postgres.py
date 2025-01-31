import psycopg2
import logging
import json
import os

config_path = os.path.join(os.path.dirname(__file__), "config.json")

if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file not found: {config_path}")


with open(config_path, "r") as file:
    config = json.load(file)

class PostgresConnectionManager:
    """
    Manages PostgreSQL database connections securely.
    """

    def __init__(self):
        """
        Load connection details from config.json.
        """
        self.host_address = config["DB_HOST"]
        self.port_number = config["DB_PORT"]
        self.database_name = config["DB_NAME"]
        self.user_name = config["DB_USER"]
        self.password = config["DB_PASSWORD"]

        err, self.connection = self.create_connection()
        if self.connection is None:
            raise Exception(err)

    def create_connection(self):
        """ Connect to PostgreSQL securely """
        con = None
        err = None
        try:
            params = {
                "host": self.host_address,
                "database": self.database_name,
                "user": self.user_name,
                "password": self.password,
                "port": self.port_number,
            }
            con = psycopg2.connect(**params)
            print("Connected to PostgreSQL successfully!")
        except Exception as err:

            print(f"Failed to connect to PostgreSQL: {err}")
            return err, con
        return err, con
    
if __name__ == "__main__":
    try:
        db_manager = PostgresConnectionManager()
        print("Database connection object created successfully.")
    except Exception as e:
        print(f"Error: {e}")
