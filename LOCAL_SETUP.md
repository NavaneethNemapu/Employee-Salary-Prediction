# Employee Salary Prediction App - Local Setup Instructions

## Prerequisites

1. **Python 3.8 or higher** installed on your system
2. **MySQL Server** installed and running
3. **Git** (optional, for cloning the repository)

## Step 1: Install MySQL and Create Database

### On Windows:
1. Download MySQL from https://dev.mysql.com/downloads/mysql/
2. Install MySQL Server
3. During installation, set root password or remember your credentials

### On macOS:
```bash
brew install mysql
brew services start mysql
```

### On Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql
```

### Create Database:
1. Log into MySQL:
```bash
mysql -u suhas -p
# Enter password: Suhas@1234
```

2. Create the database:
```sql
CREATE DATABASE employee_salary_db;
SHOW DATABASES;
EXIT;
```

## Step 2: Setup Python Environment

### Option A: Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv salary_app_env

# Activate virtual environment
# On Windows:
salary_app_env\Scripts\activate
# On macOS/Linux:
source salary_app_env/bin/activate
```

### Option B: Using System Python (not recommended)
Skip the virtual environment setup, but be aware this may cause conflicts.

## Step 3: Install Required Packages

```bash
pip install Flask==3.0.0
pip install Flask-SQLAlchemy==3.1.1
pip install Flask-Login==0.6.3
pip install Flask-WTF==1.2.1
pip install WTForms==3.1.1
pip install scikit-learn==1.3.2
pip install pandas==2.1.4
pip install numpy==1.26.2
pip install joblib==1.3.2
pip install PyMySQL==1.1.1
pip install Werkzeug==3.0.1
pip install email-validator==2.1.0
pip install gunicorn==23.0.0
```

Or install all at once:
```bash
pip install Flask==3.0.0 Flask-SQLAlchemy==3.1.1 Flask-Login==0.6.3 Flask-WTF==1.2.1 WTForms==3.1.1 scikit-learn==1.3.2 pandas==2.1.4 numpy==1.26.2 joblib==1.3.2 PyMySQL==1.1.1 Werkzeug==3.0.1 email-validator==2.1.0 gunicorn==23.0.0
```

## Step 4: Download/Clone the Application

### Option A: Download files manually
Download all project files to a folder on your computer.

### Option B: Clone from repository (if available)
```bash
git clone <repository-url>
cd employee-salary-prediction
```

## Step 5: Verify Database Connection

The application is pre-configured with your MySQL credentials:
- **Username**: suhas
- **Password**: Suhas@1234
- **Database**: employee_salary_db
- **Host**: localhost

If you need to change these, edit the `app.py` file, line 29:
```python
database_url = "mysql+pymysql://suhas:Suhas%401234@localhost/employee_salary_db"
```

## Step 6: Run the Application

### Method 1: Using Python directly
```bash
python main.py
```

### Method 2: Using Gunicorn (Production-like)
```bash
gunicorn --bind 0.0.0.0:5000 --reload main:app
```

### Method 3: Using Flask development server
```bash
export FLASK_APP=main.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

## Step 7: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

## Initial Setup

1. **First Run**: The application will automatically:
   - Create database tables
   - Train the ML model (takes 1-2 minutes)
   - Be ready for use

2. **Register Account**: Create a new user account on the registration page

3. **Make Predictions**: Use the prediction form to test salary predictions

## Troubleshooting

### Database Connection Issues:
```bash
# Test MySQL connection
mysql -u suhas -p -h localhost
# Enter password: Suhas@1234

# If connection fails, check:
# 1. MySQL server is running
# 2. Username/password are correct
# 3. Database exists
```

### Python Package Issues:
```bash
# Upgrade pip first
pip install --upgrade pip

# Then install packages one by one if bulk install fails
```

### Port Already in Use:
```bash
# Kill process using port 5000
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# On macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

### Model Training Issues:
- Ensure `data/employee_data.csv` file exists
- Check console output for detailed error messages
- Model files will be created: `salary_model.joblib` and `label_encoders.joblib`

## File Structure
```
employee-salary-prediction/
├── app.py                 # Flask application setup
├── main.py               # Application entry point
├── models.py             # Database models
├── forms.py              # Web forms
├── routes.py             # URL routes and views
├── ml_model.py           # Machine learning model
├── data/
│   └── employee_data.csv # Training dataset
├── templates/            # HTML templates
├── static/              # CSS, JS, images
└── LOCAL_SETUP.md       # This file
```

## Performance Notes

- **First startup**: Takes 1-2 minutes to train ML model
- **Subsequent startups**: Loads pre-trained model quickly
- **Database**: MySQL provides better performance than SQLite for production
- **Model accuracy**: ~82.8% with balanced predictions for both salary brackets

## Production Deployment

For production deployment, consider:
1. Using environment variables for database credentials
2. Setting `FLASK_ENV=production`
3. Using a proper WSGI server like Gunicorn with multiple workers
4. Setting up proper logging and monitoring
5. Using a reverse proxy like Nginx

## Support

If you encounter issues:
1. Check the console output for error messages
2. Verify MySQL is running and accessible
3. Ensure all required packages are installed
4. Check that port 5000 is available