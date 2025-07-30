from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with predictions
    predictions = db.relationship('Prediction', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Input features
    age = db.Column(db.Integer, nullable=False)
    workclass = db.Column(db.String(50), nullable=False)
    education = db.Column(db.String(50), nullable=False)
    marital_status = db.Column(db.String(50), nullable=False)
    occupation = db.Column(db.String(50), nullable=False)
    relationship = db.Column(db.String(50), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    hours_per_week = db.Column(db.Integer, nullable=False)
    native_country = db.Column(db.String(50), nullable=False)
    
    # Prediction result
    predicted_salary = db.Column(db.String(10), nullable=False)  # <=50K or >50K
    prediction_confidence = db.Column(db.Float)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Prediction {self.id}: {self.predicted_salary}>'
