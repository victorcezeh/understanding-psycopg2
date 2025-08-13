"""
Terminal User Interface for Student Database Queries

This module provides a simple command-line interface for querying student information
from the database. It demonstrates how to create a user-facing layer that interacts
with the database abstraction layer.

Features:
- Interactive command-line interface for user input
- Integration with custom DB class for database operations
- Formatted output display of student information
- Simple user experience for database queries

Dependencies:
- db module: Custom database management class
- Built-in input() function for user interaction

Usage:
    python terminal.py
    # Prompts user for student name and displays their favorite food
"""

# Import the custom DB class from the db module
from db import DB

class Terminal:
    """
    Terminal-based user interface for student database queries.
    
    This class provides a simple command-line interface that allows users
    to query student information by name. It acts as a presentation layer
    that interfaces with the database through the DB class.
    """
    
    def __init__(self):
        """
        Initialize the Terminal interface.
        
        Creates an instance of the DB class to handle all database
        operations. This follows the composition pattern where Terminal
        uses DB functionality without inheriting from it.
        """
        self.db = DB()  # Instantiate database handler for student queries
        
    def ask_question(self):
        """
        Interactive method to get user input and display student information.
        
        Prompts the user for a student name, queries the database using the
        DB class, and displays the formatted result. Assumes the query will
        return a tuple with student data in a specific format.
        
        Expected database record format:
        - answer[0]: student ID (not displayed)
        - answer[1]: student name
        - answer[2]: student's favorite food
        """
        # Get student name from user input
        name = input("Who do you want to know about? ")
        
        # Query database using DB class main method
        answer = self.db.main(name)
        
        # Display formatted result using tuple indexing
        # answer[1] = student name, answer[2] = favorite food
        print(f"{answer[1]} likes to eat {answer[2]}.")

# Create an instance of the Terminal class
t = Terminal()

# Execute the interactive query method
t.ask_question()