"""
Database Connection and Query Management Class

This module demonstrates an object-oriented approach to PostgreSQL database operations
using psycopg2. It encapsulates database connection management and query execution
within a reusable class structure.

Features:
- Object-oriented database connection management
- Parameterized query execution for student lookups
- Automatic resource cleanup with connection management methods
- Centralized database operations within a class

Dependencies:
- psycopg2: PostgreSQL adapter for Python
- python-dotenv: Environment variable loader

Usage:
    db = DB()
    result = db.main("Victor")  # Returns student record for Victor
"""

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration variables from environment
CLASS_ROASTER_DBNAME = os.getenv("CLASS_ROASTER_DBNAME")  # Database name
HOST = os.getenv("CLASS_ROASTER_HOST")  # Database host address
USER = os.getenv("CLASS_ROASTER_USER")  # Database username
PASSWORD = os.getenv("CLASS_ROASTER_PASSWORD")  # Database password
PORT = os.getenv("CLASS_ROASTER_PORT")  # Database port number


class DB:
    """
    Database connection and query management class.

    This class encapsulates database operations for student record retrieval,
    managing connections, cursors, and query execution in a structured way.
    """

    def __init__(self):
        """
        Initialize the DB instance with default values.

        Sets up instance variables for connection management and defines
        the parameterized query template for student lookups.
        """
        self.connection = None  # Will store the psycopg2 connection object
        self.cursor = None  # Will store the database cursor for query execution
        # Parameterized query template - %s placeholder prevents SQL injection
        self.query_template = "select * from students where name = %s"

    def initialize_connection(self):
        """
        Establish connection to the PostgreSQL database.

        Creates both the database connection and cursor objects using
        environment variables for configuration. These are stored as
        instance variables for use by other methods.
        """
        self.connection = psycopg2.connect(
            dbname=CLASS_ROASTER_DBNAME,
            user=USER,
            password=PASSWORD,
            port=PORT,
            host=HOST,
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, name):
        """
        Execute the student lookup query with the provided name.

        Args:
            name (str): The student name to search for in the database

        Returns:
            tuple or None: The first matching student record as a tuple,
                          or None if no student found with that name
        """
        # Execute parameterized query - psycopg2 handles proper escaping
        self.cursor.execute(self.query_template, (name,))
        # fetchone() returns the first row of the result set or None
        return self.cursor.fetchone()

    def close_connection(self):
        """
        Close database cursor and connection.

        Properly releases database resources by closing both the cursor
        and connection objects. Should be called after database operations
        are complete.
        """
        self.cursor.close()
        self.connection.close()

    def main(self, name):
        """
        Main method to execute a complete database lookup operation.

        Handles the full lifecycle of a database query: connection initialization,
        query execution, and cleanup. Includes basic error handling.

        Args:
            name (str): The student name to search for

        Returns:
            tuple or None: Student record if found and operation successful,
                          None if error occurs or student not found
        """
        try:
            # Establish database connection and cursor
            self.initialize_connection()
            # Execute the query and return the result
            return self.execute_query(name)
        except:
            # Basic error handling - catches any exception during database operations
            print("There was a problem!")
        finally:
            # Ensure database resources are always cleaned up
            # This runs regardless of success or failure
            self.close_connection()
