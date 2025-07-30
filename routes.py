from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from models import User, Prediction
from forms import LoginForm, RegistrationForm, PredictionForm
from ml_model import MLModel
import pandas as pd

ml_model = MLModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('dashboard')
            flash('Login successful!', 'success')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    recent_predictions = Prediction.query.filter_by(user_id=current_user.id)\
                                        .order_by(Prediction.created_at.desc())\
                                        .limit(10).all()
    
    total_predictions = Prediction.query.filter_by(user_id=current_user.id).count()
    high_salary_predictions = Prediction.query.filter_by(user_id=current_user.id, predicted_salary='>50K').count()
    
    return render_template('dashboard.html', 
                         recent_predictions=recent_predictions,
                         total_predictions=total_predictions,
                         high_salary_predictions=high_salary_predictions)

@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    form = PredictionForm()
    
    if form.validate_on_submit():
        # Prepare data for prediction
        input_data = {
            'age': form.age.data,
            'workclass': form.workclass.data,
            'education': form.education.data,
            'marital-status': form.marital_status.data,
            'occupation': form.occupation.data,
            'relationship': form.relationship.data,
            'race': form.race.data,
            'gender': form.gender.data,
            'hours-per-week': form.hours_per_week.data,
            'native-country': form.native_country.data
        }
        
        try:
            # Make prediction
            prediction, confidence = ml_model.predict(input_data)
            
            # Save prediction to database
            pred_record = Prediction()
            pred_record.user_id = current_user.id
            pred_record.age = form.age.data
            pred_record.workclass = form.workclass.data
            pred_record.education = form.education.data
            pred_record.marital_status = form.marital_status.data
            pred_record.occupation = form.occupation.data
            pred_record.relationship = form.relationship.data
            pred_record.race = form.race.data
            pred_record.gender = form.gender.data
            pred_record.hours_per_week = form.hours_per_week.data
            pred_record.native_country = form.native_country.data
            pred_record.predicted_salary = prediction
            pred_record.prediction_confidence = confidence
            
            db.session.add(pred_record)
            db.session.commit()
            
            flash(f'Prediction successful! Predicted salary bracket: {prediction}', 'success')
            return render_template('predict.html', form=form, prediction=prediction, confidence=confidence)
            
        except Exception as e:
            flash(f'Error making prediction: {str(e)}', 'danger')
    
    return render_template('predict.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
