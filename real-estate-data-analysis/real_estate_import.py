"""
Real Estate CSV Data Import Script

This script demonstrates advanced PostgreSQL database operations with psycopg2,
including CSV file processing, data type conversions, and bulk data insertion.
It imports real estate property data from a CSV file into a PostgreSQL database.

Features:
- CSV file reading and processing with DictReader
- Data type conversion and cleaning (strings, integers, decimals, timestamps)
- Timezone-aware datetime parsing
- Complex table schema with multiple data types
- Bulk data insertion with parameterized queries
- Proper error handling and resource cleanup

Dependencies:
- psycopg2: PostgreSQL adapter for Python
- python-dotenv: Environment variable loader
- python-dateutil: Advanced date/time parsing
- decimal: Precise decimal number handling
- csv: Built-in CSV file processing

Usage:
    Requires a CSV file with real estate data and proper environment configuration.
    Creates and populates a 'properties' table with comprehensive property information.
"""

import csv
import psycopg2
import os
from decimal import Decimal
from dotenv import load_dotenv
from dateutil import parser, tz

# Load environment variables from .env file
load_dotenv()

# Database configuration variables from environment
REAL_ESTATE_DBNAME = os.getenv("REAL_ESTATE_DBNAME")  # Database name for real estate data
HOST = os.getenv("HREAL_ESTATE_HOST")                 # Database host address
USER = os.getenv("REAL_ESTATE_USER")                  # Database username
PASSWORD = os.getenv("REAL_ESTATE_PASSWORD")          # Database password
PORT = int(os.getenv("REAL_ESTATE_PORT"))             # Database port (converted to integer)
PATH_TO_CSV = os.getenv("PATH_TO_CSV")                # File path to the CSV data file

# Timezone configuration for parsing date strings
# Maps "EDT" timezone abbreviation to proper timezone object
tzinfos = {"EDT": tz.gettz("America/New_York")}

def table_creation_query():
    """
    Generate SQL CREATE TABLE statement for properties table.
    
    Returns:
        str: Complete SQL CREATE TABLE statement with comprehensive schema
             including various data types (varchar, integer, decimal, timestamp)
             and a serial primary key for unique identification.
    """
    return """
    CREATE TABLE IF NOT EXISTS properties 
    (id serial PRIMARY KEY, street_address varchar, city varchar, zip_code varchar, state varchar, 
    number_of_beds integer, number_of_baths integer, square_feet integer, property_type varchar, 
    sale_date timestamp, sale_price integer, latitude decimal, longitude decimal);
"""


def clean_data(csv_row):
    """
    Clean and transform CSV row data into database-ready format.
    
    Performs data type conversions and field mapping from CSV column names
    to database column names. Handles string-to-integer conversions,
    date parsing with timezone awareness, and decimal precision for coordinates.
    
    Args:
        csv_row (dict): Raw CSV row data as dictionary with original column names
        
    Returns:
        dict: Cleaned data with proper data types and database-compatible field names
              - Strings remain as strings for address fields
              - Numeric strings converted to integers for beds, baths, square_feet
              - Date strings parsed to timezone-aware datetime objects
              - Coordinate strings converted to high-precision Decimal objects
    """
    cleaned = {}
    # Map CSV column names to database field names
    cleaned["street_address"] = csv_row["street"]
    cleaned["city"] = csv_row["city"]
    cleaned["zip_code"] = csv_row["zip"]
    cleaned["state"] = csv_row["state"]
    # Convert string numbers to integers for numeric database fields
    cleaned["number_of_beds"] = int(csv_row["beds"])
    cleaned["number_of_baths"] = int(csv_row["baths"])
    cleaned["square_feet"] = int(csv_row["sq__ft"])
    cleaned["property_type"] = csv_row["type"]
    # Parse date string with timezone information into datetime object
    cleaned["sale_date"] = parser.parse(csv_row["sale_date"], tzinfos=tzinfos)
    cleaned["sale_price"] = csv_row["price"]
    # Convert coordinate strings to Decimal for precise geographic positioning
    cleaned["latitude"] = Decimal(csv_row["latitude"])
    cleaned["longitude"] = Decimal(csv_row["longitude"])
    return cleaned
    

try:
    # Establish database connection using environment variables
    conn = psycopg2.connect(dbname=REAL_ESTATE_DBNAME, user=USER, password=PASSWORD, port=PORT, host=HOST)
    
    # Create cursor for executing database operations
    cur = conn.cursor()
    
    # Drop existing properties table for clean import (removes old data)
    cur.execute("DROP TABLE IF EXISTS properties")
    
    # Create new properties table with comprehensive schema
    cur.execute(table_creation_query())
    
    # Open and process CSV file using context manager (automatic file closure)
    with open(PATH_TO_CSV, mode="r") as csv_file:
        # DictReader treats first row as headers, returns each row as dictionary
        csv_reader = csv.DictReader(csv_file)
        
        # Process each row in the CSV file
        for row in csv_reader:
            # Clean and convert data types for database insertion
            cleaned_data = clean_data(row)
            
            # Execute parameterized INSERT query to prevent SQL injection
            # Uses %s placeholders for all 12 data fields
            cur.execute("""
                    INSERT INTO properties (
                        street_address,
                        city,
                        zip_code,
                        state,
                        number_of_beds,
                        number_of_baths,
                        square_feet,
                        property_type,
                        sale_date,
                        sale_price,
                        latitude,
                        longitude
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    # Pass cleaned data as tuple in exact order matching INSERT columns
                    cleaned_data["street_address"],
                    cleaned_data["city"],
                    cleaned_data["zip_code"],
                    cleaned_data["state"],
                    cleaned_data["number_of_beds"],
                    cleaned_data["number_of_baths"],
                    cleaned_data["square_feet"],
                    cleaned_data["property_type"],
                    cleaned_data["sale_date"],
                    cleaned_data["sale_price"],
                    cleaned_data["latitude"],
                    cleaned_data["longitude"]
                ))
            
    # Commit all INSERT operations to make changes permanent
    # Without commit(), all inserts would be rolled back
    conn.commit()
    print("Table created and data inserted successfully!")
         
except psycopg2.Error as e:
    # Handle PostgreSQL-specific errors (connection, SQL syntax, constraint violations)
    print("Database Error", e)
except Exception as e:
    # Handle other errors (file not found, data conversion errors, etc.)
    print("Unexpected Error", e)
    
finally:
    # Ensure proper cleanup of database resources
    # Closes cursor and connection even if errors occurred
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()