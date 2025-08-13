"""
Class Roster Database Management Script

This script demonstrates basic PostgreSQL database operations using psycopg2.
It creates a students table and populates it with sample student data.

Features:
- Environment variable configuration for database credentials
- Table creation with automatic primary key
- Parameterized INSERT queries for SQL injection prevention
- Proper error handling and resource cleanup

Dependencies:
- psycopg2: PostgreSQL adapter for Python
- python-dotenv: Environment variable loader
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

try:
    # Connect to an existing database
    conn = psycopg2.connect(
        dbname=CLASS_ROASTER_DBNAME, user=USER, password=PASSWORD, port=PORT, host=HOST
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Drop existing students table if it exists (clean slate approach)
    cur.execute("DROP TABLE IF EXISTS students")

    # Create student table query
    # Uses serial for auto-incrementing primary key, varchar for text fields
    student_table_creation_query = """
    CREATE TABLE IF NOT EXISTS students (id serial PRIMARY KEY, name varchar, favorite_food varchar);
    """

    # Create INSERT INTO queries using parameterized placeholders (%s)
    # Parameterized queries prevent SQL injection attacks
    insert_query_1 = """
    INSERT INTO students (name, favorite_food) VALUES (%s, %s);
    """
    insert_query_2 = """
    INSERT INTO students (name, favorite_food) VALUES (%s, %s);
    """
    insert_query_3 = """
    INSERT INTO students (name, favorite_food) VALUES (%s, %s);
    """

    # Execute a command to create a new table
    cur.execute(student_table_creation_query)

    # Execute commands to insert into student table
    # Second parameter is a tuple containing the actual values to insert
    cur.execute(insert_query_1, ("Victor", "Chicken"))
    cur.execute(insert_query_2, ("Esan", "Rice"))
    cur.execute(insert_query_3, ("Pelumi", "Beans"))

    # Make the changes to the database persistent
    # Without commit(), changes are only temporary in the transaction
    conn.commit()
    print("Table created and data inserted successfully!")

except psycopg2.Error as e:
    # Handle PostgreSQL-specific errors (connection issues, SQL errors, etc.)
    print("Database Error:", e)

except Exception as e:
    # Handle any other unexpected errors
    print("Unexpected Error", e)

finally:
    # Close all connections with the database
    # Ensures proper cleanup even if errors occur
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
