#!/usr/bin/env python3
"""
Local development server for Employee Salary Prediction App
This script sets up and runs the Flask application locally
"""

import os
import sys
import subprocess

def check_mysql_connection():
    """Check if MySQL connection is working"""
    try:
        import pymysql
        connection = pymysql.connect(
            host='localhost',
            user='suhas',
            password='Suhas@1234',
            database='employee_salary_db',
            charset='utf8mb4'
        )
        connection.close()
        print("✓ MySQL connection successful")
        return True
    except ImportError:
        print("✗ PyMySQL not installed. Run: pip install pymysql")
        return False
    except Exception as e:
        print(f"✗ MySQL connection failed: {e}")
        print("Run 'python setup_database.py' to create the database")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'flask', 'flask_sqlalchemy', 'flask_login', 'flask_wtf',
        'sklearn', 'pandas', 'numpy', 'joblib', 'pymysql'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("✗ Missing required packages:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\nInstall with: pip install " + " ".join(missing_packages))
        return False
    
    print("✓ All required packages installed")
    return True

def main():
    print("Employee Salary Prediction - Local Development Server")
    print("=" * 55)
    
    # Check dependencies
    print("\n1. Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    
    # Check MySQL connection
    print("\n2. Checking MySQL connection...")
    if not check_mysql_connection():
        sys.exit(1)
    
    # Set environment variables
    os.environ['FLASK_ENV'] = 'development'
    os.environ['SESSION_SECRET'] = 'dev-secret-key-change-in-production'
    
    print("\n3. Starting Flask development server...")
    print("   Server will be available at: http://localhost:5000")
    print("   Press Ctrl+C to stop the server")
    print("-" * 55)
    
    # Run the application
    try:
        from main import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except Exception as e:
        print(f"\nError starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()