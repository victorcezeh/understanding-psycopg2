# Class Roster Database Project

A comprehensive demonstration of PostgreSQL database operations using psycopg2, showcasing the progression from basic database operations to object-oriented design and user interface implementation.

## Project Overview

This project demonstrates fundamental database concepts through a simple class roster system that stores and retrieves student information including names and favorite foods. The implementation progresses through three distinct approaches, each building upon the previous one to show different programming paradigms and database interaction patterns.

## Features

- **Database Schema Management**: Automatic table creation and data population
- **Parameterized Queries**: SQL injection prevention through proper query parameterization
- **Object-Oriented Design**: Database operations encapsulated in reusable classes
- **User Interface**: Interactive command-line interface for database queries
- **Error Handling**: Comprehensive exception handling and resource cleanup
- **Environment Configuration**: Secure credential management using environment variables

## Prerequisites

Before running this project, ensure you have:

- Python 3.x installed
- PostgreSQL database server running
- Required Python packages (see Installation section)
- Database credentials configured in environment variables

## Installation

1. **Install required packages:**
```bash
pip install psycopg2-binary python-dotenv
```

2. **Create environment file (.env):**
```env
CLASS_ROASTER_DBNAME=your_database_name
CLASS_ROASTER_HOST=localhost
CLASS_ROASTER_USER=your_username
CLASS_ROASTER_PASSWORD=your_password
CLASS_ROASTER_PORT=5432
```

3. **Ensure PostgreSQL is running and accessible with the provided credentials**

## Project Structure

The project consists of three main components that demonstrate different approaches to database interaction:

### 1. Basic Database Operations (`class_roster_basic.py`)

**Purpose**: Demonstrates fundamental psycopg2 operations using a procedural approach.

**Key Concepts**:
- Direct database connection management
- Table creation with DDL operations
- Parameterized INSERT queries for data safety
- Manual transaction management with commit/rollback
- Proper resource cleanup with try/except/finally blocks

**What it does**:
- Connects to PostgreSQL database
- Drops existing `students` table (if exists)
- Creates new `students` table with auto-incrementing ID
- Inserts three sample student records
- Commits changes and closes connections

**Usage**:
```bash
python class_roster_basic.py
```

### 2. Object-Oriented Database Class (`db.py`)

**Purpose**: Encapsulates database operations within a reusable class structure.

**Key Concepts**:
- Object-oriented database connection management
- Method-based operation separation
- Instance variable management for connections
- Centralized query execution and result handling
- Class-based error handling and cleanup

**What it does**:
- Provides `DB` class for student record queries
- Manages database connections as instance variables
- Implements parameterized query execution
- Returns individual student records by name lookup
- Handles complete operation lifecycle (connect → query → cleanup)

**Usage**:
```python
from db import DB
db = DB()
student_data = db.main("Victor")
```

### 3. Terminal User Interface (`terminal.py`)

**Purpose**: Creates a user-friendly command-line interface for database interactions.

**Key Concepts**:
- Separation of concerns between UI and data layers
- Composition pattern (Terminal uses DB functionality)
- Interactive user input handling
- Formatted output presentation
- Integration between interface and database layers

**What it does**:
- Provides interactive command-line interface
- Prompts user for student name input
- Queries database through DB class integration
- Displays formatted student information
- Handles the complete user interaction flow

**Usage**:
```bash
python terminal.py
```

## Database Schema

The project uses a simple `students` table with the following structure:

```sql
CREATE TABLE students (
    id serial PRIMARY KEY,
    name varchar,
    favorite_food varchar
);
```

**Sample Data**:
- Victor - Chicken
- Esan - Rice  
- Pelumi - Beans

## Learning Progression

This project demonstrates a clear learning progression in database programming:

1. **Procedural Approach**: Direct database operations with manual resource management
2. **Object-Oriented Design**: Encapsulation of database logic in reusable classes
3. **User Interface Integration**: Building interactive applications on top of database abstractions

## Key psycopg2 Concepts Demonstrated

- **Connection Management**: Establishing and maintaining database connections
- **Cursor Operations**: Using cursors for query execution and result retrieval
- **Parameterized Queries**: Preventing SQL injection through proper query parameterization
- **Transaction Control**: Manual commit/rollback for data consistency
- **Error Handling**: Catching and handling psycopg2-specific exceptions
- **Resource Cleanup**: Proper connection and cursor closure

## Security Considerations

- **Environment Variables**: Database credentials stored securely outside source code
- **Parameterized Queries**: All user input properly escaped to prevent SQL injection
- **Connection String Security**: Credentials not hardcoded in application files

## Troubleshooting

**Common Issues**:

1. **Connection Refused**: Verify PostgreSQL is running and accessible
2. **Authentication Failed**: Check username/password in .env file
3. **Database Not Found**: Ensure database exists or has proper permissions
4. **Module Import Errors**: Verify all required packages are installed

**Environment Variable Issues**:
- Ensure .env file is in the same directory as your Python scripts
- Verify all required environment variables are defined
- Check for typos in environment variable names

## Next Steps

This foundation can be extended with:
- Additional CRUD operations (UPDATE, DELETE)
- More complex queries with JOINs and aggregations
- Connection pooling for production applications
- Web interface using Flask/Django
- Data validation and input sanitization
- Advanced error handling and logging

## Contributing

This is a learning project demonstrating psycopg2 fundamentals. Feel free to extend it with additional features or use it as a foundation for more complex database applications.