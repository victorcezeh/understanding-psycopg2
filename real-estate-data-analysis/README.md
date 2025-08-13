# Real Estate Data Analysis Project

A comprehensive demonstration of advanced PostgreSQL operations using psycopg2 for real estate data processing and analysis. This project showcases CSV data import, complex data type handling, and business intelligence queries for property market analysis.

## Project Overview

This project demonstrates advanced database operations through a real estate data analysis system that imports property data from CSV files and performs analytical queries to answer business questions. The implementation shows progression from data import and transformation to analytical query execution for market insights.

## Features

- **CSV Data Import**: Automated bulk data loading from external CSV files
- **Complex Data Types**: Handling timestamps, decimals, integers, and geographic coordinates
- **Data Transformation**: CSV field mapping and data type conversion pipeline
- **Timezone Support**: Proper handling of timezone-aware datetime data
- **Business Analytics**: SQL aggregate functions for market analysis
- **Geographic Data**: Precise latitude/longitude storage using decimal precision
- **Production-Ready Error Handling**: Comprehensive exception management for data processing

## Prerequisites

Before running this project, ensure you have:

- Python 3.x installed
- PostgreSQL database server running
- Real estate CSV data file with proper format
- Required Python packages (see Installation section)
- Database credentials configured in environment variables

## Installation

1. **Install required packages:**
```bash
pip install psycopg2-binary python-dotenv python-dateutil
```

2. **Create environment file (.env):**
```env
REAL_ESTATE_DBNAME=your_database_name
HREAL_ESTATE_HOST=localhost
REAL_ESTATE_USER=your_username
REAL_ESTATE_PASSWORD=your_password
REAL_ESTATE_PORT=5432
PATH_TO_CSV=/path/to/your/properties.csv
```

3. **Prepare CSV data file with the following columns:**
   - street, city, zip, state, beds, baths, sq__ft, type, sale_date, price, latitude, longitude

## Project Structure

The project consists of two main components that demonstrate different aspects of data processing and analysis:

### 1. CSV Data Import Pipeline (`real_estate_import.py`)

**Purpose**: Demonstrates advanced data import operations with complex data type handling and transformation.

**Key Concepts**:
- **CSV Processing**: Using `csv.DictReader` for header-based data access
- **Data Type Conversion**: String-to-integer, string-to-decimal, and date parsing
- **Timezone Handling**: Parsing timezone-aware datetime strings with dateutil
- **Decimal Precision**: High-precision geographic coordinate storage
- **Bulk Data Operations**: Efficient row-by-row insertion with proper error handling
- **Schema Management**: Dynamic table creation with complex column types

**Data Transformation Pipeline**:
```python
CSV Row → clean_data() → Type Conversion → Database Insert
```

**What it does**:
- Drops and recreates `properties` table with comprehensive schema
- Opens CSV file and processes each row using DictReader
- Transforms raw CSV data through `clean_data()` function:
  - Maps CSV column names to database field names
  - Converts string numbers to appropriate integer types
  - Parses date strings with timezone information
  - Converts coordinate strings to high-precision Decimal objects
- Executes parameterized INSERT queries for each property record
- Commits all changes as a single transaction

**Database Schema Created**:
```sql
CREATE TABLE properties (
    id serial PRIMARY KEY,
    street_address varchar,
    city varchar,
    zip_code varchar,
    state varchar,
    number_of_beds integer,
    number_of_baths integer,
    square_feet integer,
    property_type varchar,
    sale_date timestamp,
    sale_price integer,
    latitude decimal,
    longitude decimal
);
```

**Usage**:
```bash
python real_estate_import.py
```

### 2. Property Price Analysis (`property_analysis.py`)

**Purpose**: Demonstrates SQL aggregate functions and analytical queries for business intelligence.

**Key Concepts**:
- **Aggregate Functions**: Using AVG() and ROUND() for statistical analysis
- **GROUP BY Operations**: Data categorization for comparative analysis
- **Business Intelligence**: Answering specific market questions with data
- **Connection String Format**: Alternative psycopg2 connection syntax
- **Result Processing**: Handling aggregate query results

**Business Question Addressed**:
*"Are single family homes and condos more expensive on average?"*

**What it does**:
- Connects to database using concise connection string format
- Executes analytical query with GROUP BY and aggregate functions
- Calculates average sale price for each property type
- Rounds averages to whole numbers for readability
- Returns comparative pricing data across property types

**SQL Query Executed**:
```sql
SELECT property_type, ROUND(AVG(sale_price)) 
FROM properties 
GROUP BY property_type;
```

**Expected Output Format**:
```
[('Condo', Decimal('102944')), ('Residential', Decimal('92752'))]
```

**Usage**:
```bash
python property_analysis.py
```

## CSV Data Format

The project expects a CSV file with the following column structure:

| Column | Description | Example |
|--------|-------------|---------|
| street | Street address | "123 Main St" |
| city | City name | "New York" |
| zip | ZIP code | "10001" |
| state | State abbreviation | "NY" |
| beds | Number of bedrooms | "3" |
| baths | Number of bathrooms | "2" |
| sq__ft | Square footage | "1500" |
| type | Property type | "Residential" |
| sale_date | Sale date with timezone | "2023-06-15 EDT" |
| price | Sale price | "450000" |
| latitude | Geographic latitude | "40.7128" |
| longitude | Geographic longitude | "-74.0060" |

## Data Processing Pipeline

The project implements a comprehensive ETL (Extract, Transform, Load) pipeline:

### Extract
- CSV file reading with automatic header detection
- Row-by-row processing for memory efficiency
- File handling with proper resource management

### Transform
- **Field Mapping**: CSV columns → Database columns
- **Type Conversion**: 
  - Strings → Integers (beds, baths, square_feet)
  - Strings → Decimals (coordinates)
  - Date strings → Timezone-aware datetime objects
- **Data Validation**: Implicit validation through type conversion
- **Geographic Processing**: High-precision coordinate handling

### Load
- Parameterized INSERT queries for security
- Transaction-based loading for data integrity
- Comprehensive error handling for data quality issues

## Advanced psycopg2 Features Demonstrated

### Data Type Handling
- **Serial Primary Keys**: Auto-incrementing unique identifiers
- **Varchar Fields**: Variable-length text storage
- **Integer Types**: Numeric data for counts and measurements
- **Decimal Precision**: High-accuracy geographic coordinates
- **Timestamp with Timezone**: Proper datetime storage

### Query Patterns
- **DDL Operations**: Dynamic table creation and schema management
- **Bulk INSERT Operations**: Efficient data loading patterns
- **Aggregate Queries**: Statistical analysis with GROUP BY
- **Parameterized Queries**: SQL injection prevention

### Connection Management
- **Connection String Format**: Alternative connection syntax
- **Transaction Control**: Commit/rollback for data consistency
- **Resource Cleanup**: Proper cursor and connection closure

## Business Intelligence Capabilities

The analysis component demonstrates how to use SQL for market research:

- **Comparative Analysis**: Average pricing across property types
- **Market Segmentation**: Grouping properties by characteristics
- **Statistical Functions**: Mean calculations for market trends
- **Data Aggregation**: Summarizing large datasets for insights

## Error Handling Strategy

The project implements production-ready error handling:

- **Database Errors**: psycopg2-specific exception handling
- **File Processing Errors**: CSV parsing and file access issues
- **Data Conversion Errors**: Type conversion and validation failures
- **Resource Management**: Guaranteed cleanup in finally blocks

## Performance Considerations

- **Memory Efficiency**: Row-by-row CSV processing instead of loading entire file
- **Transaction Batching**: Single commit for entire import operation
- **Index Usage**: Serial primary key provides efficient lookups
- **Data Types**: Appropriate types chosen for storage efficiency

## Troubleshooting

**Common Issues**:

1. **CSV Format Mismatch**: Verify column names match expected format
2. **Date Parsing Errors**: Check timezone format in sale_date column
3. **Numeric Conversion Errors**: Ensure beds, baths, sq__ft contain valid numbers
4. **File Path Issues**: Verify PATH_TO_CSV environment variable is correct
5. **Coordinate Precision**: Large decimal values may cause overflow

**Data Quality Checks**:
- Verify CSV has proper headers
- Check for missing or null values in required fields
- Validate date formats include timezone information
- Ensure numeric fields contain parseable values

## Sample Queries

After running the import, you can perform various analytical queries:

```sql
-- Average price by number of bedrooms
SELECT number_of_beds, ROUND(AVG(sale_price)) as avg_price
FROM properties 
GROUP BY number_of_beds 
ORDER BY number_of_beds;

-- Properties by city with price range
SELECT city, COUNT(*) as property_count, 
       MIN(sale_price) as min_price, 
       MAX(sale_price) as max_price
FROM properties 
GROUP BY city;

-- Recent sales (last 30 days)
SELECT street_address, city, sale_price, sale_date
FROM properties 
WHERE sale_date >= NOW() - INTERVAL '30 days'
ORDER BY sale_date DESC;
```

## Next Steps

This foundation can be extended with:

- **Advanced Analytics**: Price per square foot, market trends over time
- **Geographic Queries**: PostGIS integration for spatial analysis
- **Data Visualization**: Integration with matplotlib or plotly
- **API Development**: RESTful endpoints for property search
- **Data Validation**: Comprehensive input validation and cleaning
- **Performance Optimization**: Bulk insert operations and indexing strategies
- **Real-time Updates**: Streaming data processing for live market data

## Contributing

This is a learning project demonstrating advanced psycopg2 features for real-world data processing scenarios. The code showcases production-ready patterns for CSV import, data transformation, and business intelligence queries that can be adapted for various data analysis projects.