# Employee Salary Prediction Application

## Overview

This is a Flask-based web application that predicts whether an employee's salary will be above or below $50K based on demographic and employment data. The application uses machine learning (Random Forest) to make predictions and includes user authentication, a dashboard for viewing prediction history, and a clean web interface.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **UI Framework**: Bootstrap 5 with dark theme
- **Icons**: Feather Icons
- **Styling**: Custom CSS with Bootstrap overrides
- **JavaScript**: Vanilla JavaScript for form validation and UI interactions

### Backend Architecture
- **Framework**: Flask (Python microframework)
- **Architecture Pattern**: Modular Flask application with separate files for routes, models, forms, and ML logic
- **Session Management**: Flask-Login for user authentication
- **Security**: Password hashing with Werkzeug, CSRF protection with Flask-WTF

### Database Architecture
- **ORM**: SQLAlchemy with Flask-SQLAlchemy
- **Database**: MySQL with PyMySQL driver (also supports PostgreSQL via environment variable)
- **Default Credentials**: Username: suhas, Password: Suhas@1234, Database: employee_salary_db
- **Models**: User and Prediction entities with one-to-many relationship

## Key Components

### Authentication System
- User registration and login functionality
- Password hashing for security
- Session-based authentication with Flask-Login
- Protected routes requiring user authentication

### Machine Learning Pipeline
- **Model**: Random Forest Classifier using scikit-learn
- **Data Processing**: Label encoding for categorical features, StandardScaler for numerical features
- **Features**: Age, workclass, education, marital status, occupation, relationship, race, gender, hours per week, native country
- **Target**: Binary classification (≤50K or >50K salary)
- **Model Persistence**: Joblib for saving/loading trained models

### Web Interface
- **Landing Page**: Hero section with call-to-action buttons
- **Dashboard**: Statistics overview and prediction history
- **Prediction Form**: Multi-field form for input data
- **Results Display**: Visual prediction results with confidence scores

### Form Handling
- **Form Library**: Flask-WTF with WTForms
- **Validation**: Client-side and server-side validation
- **Field Types**: Text inputs, dropdowns, number inputs with appropriate validators

## Data Flow

1. **User Registration/Login**: User creates account or signs in
2. **Data Input**: User fills out prediction form with employee characteristics
3. **Data Processing**: Form data is validated and preprocessed (encoding, scaling)
4. **Prediction**: ML model processes the data and returns prediction with confidence
5. **Storage**: Prediction results are stored in database linked to user
6. **Display**: Results are shown to user with visual indicators and confidence metrics

## External Dependencies

### Python Packages
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **joblib**: Model serialization
- **Werkzeug**: WSGI utilities and security

### Frontend Dependencies
- **Bootstrap 5**: CSS framework with dark theme
- **Feather Icons**: SVG icon library
- **Custom CSS**: Application-specific styling

### Data Requirements
- **Training Data**: CSV file with employee salary dataset
- **Features**: Demographic and employment-related columns
- **Format**: Standard adult census dataset format

## Deployment Strategy

### Environment Configuration
- **Database URL**: Configurable via `DATABASE_URL` environment variable
- **Session Secret**: Configurable via `SESSION_SECRET` environment variable
- **Debug Mode**: Enabled in development, should be disabled in production

### Application Structure
- **Entry Point**: `main.py` runs the Flask application
- **Configuration**: Environment-based configuration in `app.py`
- **Proxy Support**: ProxyFix middleware for deployment behind reverse proxies

### Database Initialization
- **Auto-creation**: Tables are automatically created on first run
- **Model Training**: ML model is trained automatically on application startup (82.8% accuracy)
- **Data Persistence**: MySQL database for production-ready performance, also supports PostgreSQL
- **Local Setup**: Includes setup_database.py script for easy MySQL database creation

### Static Assets
- **CSS**: Custom styling in `/static/css/`
- **JavaScript**: Client-side functionality in `/static/js/`
- **Templates**: Jinja2 templates in `/templates/` directory

The application is designed to be easily deployable on platforms like Replit, with minimal configuration required for basic functionality. The modular structure allows for easy maintenance and feature additions.