"""
Class Roster Database Management Script

This script demonstrates basic PostgreSQL database operations using psycopg2.
It creates a students table and populates it with sample student data.

Features:
- Environment variable configuration for database credentials
- Table creation with automatic primary key
- Batch INSERT operations using executemany() for efficiency
- Parameterized queries for SQL injection prevention
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
    # Establish connection to PostgreSQL database using environment variables
    conn = psycopg2.connect(
        dbname=CLASS_ROASTER_DBNAME, user=USER, password=PASSWORD, port=PORT, host=HOST
    )

    # Create cursor object to execute database commands
    cur = conn.cursor()

    # Drop existing students table if it exists (ensures clean slate)
    cur.execute("DROP TABLE IF EXISTS students")

    # Define table creation query
    # Uses SERIAL for auto-incrementing primary key, VARCHAR for text columns
    student_table_creation_query = """
    CREATE TABLE IF NOT EXISTS students (id serial PRIMARY KEY, name varchar, favorite_food varchar);
    """

    # Define parameterized INSERT query template
    # Uses %s placeholders to prevent SQL injection attacks
    insert_query = """
    INSERT INTO students (name, favorite_food) VALUES (%s, %s);
    """
    
    # Execute table creation command
    cur.execute(student_table_creation_query)
    
    # Sample student data as list of tuples
    # Each tuple contains (name, favorite_food) for one student
    students = [
        ("Victor", "Chicken"),
        ("Esan", "Rice"),
        ("Pelumi", "Beans")
    ]

    # Batch insert all student records using executemany()
    # More efficient than individual execute() calls for multiple records
    cur.executemany(insert_query, students)

    # Commit transaction to make changes permanent in database
    # Without commit(), all changes remain in temporary transaction state
    conn.commit()
    print("Table created and data inserted successfully!")

except psycopg2.Error as e:
    # Handle PostgreSQL-specific errors (connection, authentication, SQL syntax, etc.)
    print("Database Error:", e)

except Exception as e:
    # Catch any other unexpected errors not related to PostgreSQL
    print("Unexpected Error:", e)

finally:
    # Ensure proper cleanup of database resources
    # Close cursor and connection even if errors occurred
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()