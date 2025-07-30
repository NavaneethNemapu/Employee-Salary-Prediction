from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PredictionForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=17, max=90)])
    
    workclass = SelectField('Work Class', validators=[DataRequired()], choices=[
        ('Private', 'Private'),
        ('Self-emp-not-inc', 'Self-employed (not incorporated)'),
        ('Self-emp-inc', 'Self-employed (incorporated)'),
        ('Federal-gov', 'Federal Government'),
        ('Local-gov', 'Local Government'),
        ('State-gov', 'State Government'),
        ('Without-pay', 'Without Pay'),
        ('Never-worked', 'Never Worked')
    ])
    
    education = SelectField('Education', validators=[DataRequired()], choices=[
        ('Bachelors', 'Bachelors'),
        ('Some-college', 'Some College'),
        ('11th', '11th Grade'),
        ('HS-grad', 'High School Graduate'),
        ('Prof-school', 'Professional School'),
        ('Assoc-acdm', 'Associate Academic'),
        ('Assoc-voc', 'Associate Vocational'),
        ('9th', '9th Grade'),
        ('7th-8th', '7th-8th Grade'),
        ('12th', '12th Grade'),
        ('Masters', 'Masters'),
        ('1st-4th', '1st-4th Grade'),
        ('10th', '10th Grade'),
        ('Doctorate', 'Doctorate'),
        ('5th-6th', '5th-6th Grade'),
        ('Preschool', 'Preschool')
    ])
    
    marital_status = SelectField('Marital Status', validators=[DataRequired()], choices=[
        ('Married-civ-spouse', 'Married (civilian spouse)'),
        ('Divorced', 'Divorced'),
        ('Never-married', 'Never Married'),
        ('Separated', 'Separated'),
        ('Widowed', 'Widowed'),
        ('Married-spouse-absent', 'Married (spouse absent)'),
        ('Married-AF-spouse', 'Married (Armed Forces spouse)')
    ])
    
    occupation = SelectField('Occupation', validators=[DataRequired()], choices=[
        ('Tech-support', 'Technical Support'),
        ('Craft-repair', 'Craft & Repair'),
        ('Other-service', 'Other Service'),
        ('Sales', 'Sales'),
        ('Exec-managerial', 'Executive/Managerial'),
        ('Prof-specialty', 'Professional Specialty'),
        ('Handlers-cleaners', 'Handlers & Cleaners'),
        ('Machine-op-inspct', 'Machine Operator/Inspector'),
        ('Adm-clerical', 'Administrative/Clerical'),
        ('Farming-fishing', 'Farming & Fishing'),
        ('Transport-moving', 'Transportation & Moving'),
        ('Priv-house-serv', 'Private House Service'),
        ('Protective-serv', 'Protective Service'),
        ('Armed-Forces', 'Armed Forces')
    ])
    
    relationship = SelectField('Relationship', validators=[DataRequired()], choices=[
        ('Wife', 'Wife'),
        ('Own-child', 'Own Child'),
        ('Husband', 'Husband'),
        ('Not-in-family', 'Not in Family'),
        ('Other-relative', 'Other Relative'),
        ('Unmarried', 'Unmarried')
    ])
    
    race = SelectField('Race', validators=[DataRequired()], choices=[
        ('White', 'White'),
        ('Asian-Pac-Islander', 'Asian-Pacific Islander'),
        ('Amer-Indian-Eskimo', 'American Indian-Eskimo'),
        ('Other', 'Other'),
        ('Black', 'Black')
    ])
    
    gender = SelectField('Gender', validators=[DataRequired()], choices=[
        ('Female', 'Female'),
        ('Male', 'Male')
    ])
    
    hours_per_week = IntegerField('Hours per Week', validators=[DataRequired(), NumberRange(min=1, max=99)])
    
    native_country = SelectField('Native Country', validators=[DataRequired()], choices=[
        ('United-States', 'United States'),
        ('Cambodia', 'Cambodia'),
        ('England', 'England'),
        ('Puerto-Rico', 'Puerto Rico'),
        ('Canada', 'Canada'),
        ('Germany', 'Germany'),
        ('Outlying-US(Guam-USVI-etc)', 'Outlying US'),
        ('India', 'India'),
        ('Japan', 'Japan'),
        ('Greece', 'Greece'),
        ('South', 'South'),
        ('China', 'China'),
        ('Cuba', 'Cuba'),
        ('Iran', 'Iran'),
        ('Honduras', 'Honduras'),
        ('Philippines', 'Philippines'),
        ('Italy', 'Italy'),
        ('Poland', 'Poland'),
        ('Jamaica', 'Jamaica'),
        ('Vietnam', 'Vietnam'),
        ('Mexico', 'Mexico'),
        ('Portugal', 'Portugal'),
        ('Ireland', 'Ireland'),
        ('France', 'France'),
        ('Dominican-Republic', 'Dominican Republic'),
        ('Laos', 'Laos'),
        ('Ecuador', 'Ecuador'),
        ('Taiwan', 'Taiwan'),
        ('Haiti', 'Haiti'),
        ('Columbia', 'Columbia'),
        ('Hungary', 'Hungary'),
        ('Guatemala', 'Guatemala'),
        ('Nicaragua', 'Nicaragua'),
        ('Scotland', 'Scotland'),
        ('Thailand', 'Thailand'),
        ('Yugoslavia', 'Yugoslavia'),
        ('El-Salvador', 'El Salvador'),
        ('Trinadad&Tobago', 'Trinidad & Tobago'),
        ('Peru', 'Peru'),
        ('Hong', 'Hong Kong'),
        ('Holand-Netherlands', 'Netherlands')
    ])
    
    submit = SubmitField('Predict Salary')
