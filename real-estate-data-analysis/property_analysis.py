"""
Real Estate Property Price Analysis Script

This script demonstrates SQL aggregate functions and GROUP BY operations using psycopg2
to analyze average property prices by property type. It answers the business question:
"Are single family homes and condos more expensive on average?"

Features:
- SQL aggregate function usage (AVG, ROUND)
- GROUP BY clause for data categorization
- Business intelligence query execution
- Simplified connection string format
- Direct result display without extensive formatting

Dependencies:
- psycopg2: PostgreSQL adapter for Python
- python-dotenv: Environment variable loader

Usage:
    Requires an existing 'properties' table with sale_price and property_type columns.
    Outputs average sale prices grouped by property type.
"""

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration variables from environment
REAL_ESTATE_DBNAME = os.getenv("REAL_ESTATE_DBNAME")  # Database name for real estate data
USER = os.getenv("REAL_ESTATE_USER")                  # Database username
PASSWORD = os.getenv("REAL_ESTATE_PASSWORD")          # Database password

# Business question being answered through data analysis
# Are single family homes or condos more expensive on average?

# Establish database connection using connection string format
# Alternative to keyword argument format: more concise but less explicit
conn = psycopg2.connect(f"dbname={REAL_ESTATE_DBNAME} user={USER} password={PASSWORD}")

# Create cursor for executing database operations
cur = conn.cursor()

# Execute analytical query using SQL aggregate functions
# - GROUP BY property_type: Groups all records by property type (Single Family, Condo, etc.)
# - AVG(sale_price): Calculates average sale price for each property type group
# - ROUND(): Rounds the average to nearest whole number for readability
cur.execute("select property_type, round(avg(sale_price)) from properties group by property_type;")

# Fetch all results from the executed query
# Returns list of tuples: [(property_type1, avg_price1), (property_type2, avg_price2), ...]
result = cur.fetchall()

# Display the analytical results
# Shows property types and their corresponding average sale prices
print(result)