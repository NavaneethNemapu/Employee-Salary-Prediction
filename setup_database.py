#!/usr/bin/env python3
"""
Database setup script for Employee Salary Prediction App
Run this script to create the MySQL database and verify connection
"""

import pymysql
import sys

def create_database():
    """Create the employee_salary_db database if it doesn't exist"""
    try:
        # Connect to MySQL server (without specifying database)
        connection = pymysql.connect(
            host='localhost',
            user='suhas',
            password='Suhas@1234',
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS employee_salary_db")
        print("✓ Database 'employee_salary_db' created successfully!")
        
        # List databases to confirm
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("\nAvailable databases:")
        for db in databases:
            print(f"  - {db[0]}")
        
        cursor.close()
        connection.close()
        return True
        
    except pymysql.Error as e:
        print(f"✗ MySQL Error: {e}")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_connection():
    """Test connection to the employee_salary_db database"""
    try:
        connection = pymysql.connect(
            host='localhost',
            user='suhas',
            password='Suhas@1234',
            database='employee_salary_db',
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✓ Connected to MySQL version: {version[0]}")
        
        cursor.close()
        connection.close()
        return True
        
    except pymysql.Error as e:
        print(f"✗ Connection failed: {e}")
        return False

def main():
    print("Employee Salary Prediction - Database Setup")
    print("=" * 50)
    
    print("\n1. Creating database...")
    if not create_database():
        print("Database creation failed. Please check your MySQL installation and credentials.")
        sys.exit(1)
    
    print("\n2. Testing connection...")
    if not test_connection():
        print("Connection test failed. Please verify your MySQL setup.")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✓ Database setup completed successfully!")
    print("✓ You can now run the Flask application with: python main.py")
    print("✓ The app will be available at: http://localhost:5000")

if __name__ == "__main__":
    main()