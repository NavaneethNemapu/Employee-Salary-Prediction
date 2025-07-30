import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import logging

class MLModel:
    def __init__(self):
        self.model = None
        self.label_encoders = {}

        self.feature_columns = ['age', 'workclass', 'education', 'marital-status', 'occupation', 
                               'relationship', 'race', 'gender', 'hours-per-week', 'native-country']
        self.model_path = 'salary_model.joblib'
        self.encoders_path = 'label_encoders.joblib'

        
        # Load existing model if available
        self.load_model()
    
    def load_data(self):
        """Load and preprocess the employee salary dataset"""
        try:
            # Load the dataset
            df = pd.read_csv('data/employee_data.csv')
            
            # Clean the data
            df = df.replace('?', np.nan)
            df = df.dropna()
            
            # Remove leading/trailing spaces
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].str.strip()
            
            logging.info(f"Dataset loaded successfully. Shape: {df.shape}")
            return df
            
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            return None
    
    def preprocess_data(self, df, is_training=True):
        """Preprocess the data for training or prediction"""
        try:
            # Select features
            X = df[self.feature_columns].copy()
            
            # Encode categorical variables
            for column in X.columns:
                if X[column].dtype == 'object':
                    if is_training:
                        le = LabelEncoder()
                        # Handle missing values by replacing with a placeholder
                        X[column] = X[column].fillna('Unknown')
                        X[column] = le.fit_transform(X[column])
                        self.label_encoders[column] = le
                    else:
                        if column in self.label_encoders:
                            # Handle unseen categories and missing values
                            le = self.label_encoders[column]
                            X[column] = X[column].fillna('Unknown')
                            
                            def encode_value(x):
                                try:
                                    if x in le.classes_:
                                        return le.transform([x])[0]
                                    else:
                                        # Return a default value for unseen categories
                                        return len(le.classes_)
                                except:
                                    return len(le.classes_)
                            
                            X[column] = X[column].map(encode_value)
                        else:
                            X[column] = 0
            
            # Don't scale the data - Random Forest works better with raw encoded values
            return X
            
        except Exception as e:
            logging.error(f"Error preprocessing data: {str(e)}")
            return None
    
    def train_model(self):
        """Train the machine learning model"""
        if os.path.exists(self.model_path):
            logging.info("Model already exists. Skipping training.")
            return
        
        try:
            # Load data
            df = self.load_data()
            if df is None:
                logging.error("Cannot train model: data loading failed")
                return
            
            logging.info(f"Training data shape: {df.shape}")
            logging.info(f"Target distribution:\n{df['income'].value_counts()}")
            
            # Prepare features and target
            X = self.preprocess_data(df, is_training=True)
            if X is None:
                logging.error("Data preprocessing failed")
                return
                
            y = df['income'].str.strip()
            
            logging.info(f"Processed features shape: {X.shape}")
            logging.info(f"Features: {X.columns.tolist()}")
            
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Train Random Forest model with better parameters
            self.model = RandomForestClassifier(
                n_estimators=200,
                random_state=42,
                max_depth=15,
                min_samples_split=10,
                min_samples_leaf=4,
                class_weight='balanced'  # Handle class imbalance
            )
            
            logging.info("Training Random Forest model...")
            self.model.fit(X_train, y_train)
            
            # Evaluate the model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            logging.info(f"Model trained successfully!")
            logging.info(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
            logging.info(f"Accuracy: {accuracy:.4f}")
            logging.info(f"Classification Report:\n{classification_report(y_test, y_pred)}")
            
            # Check feature importance
            feature_importance = pd.DataFrame({
                'feature': X.columns,
                'importance': self.model.feature_importances_
            }).sort_values('importance', ascending=False)
            logging.info(f"Top 5 most important features:\n{feature_importance.head()}")
            
            # Save the model and preprocessors
            self.save_model()
            
        except Exception as e:
            logging.error(f"Error training model: {str(e)}")
            import traceback
            logging.error(traceback.format_exc())
    
    def predict(self, input_data):
        """Make prediction for new data"""
        try:
            if self.model is None:
                raise ValueError("Model not trained or loaded")
            
            # Convert input to DataFrame
            df_input = pd.DataFrame([input_data])
            
            # Preprocess the input
            X_processed = self.preprocess_data(df_input, is_training=False)
            
            # Make prediction
            prediction = self.model.predict(X_processed)[0]
            prediction_proba = self.model.predict_proba(X_processed)[0]
            
            # Get confidence (max probability)
            confidence = float(max(prediction_proba))
            
            logging.info(f"Prediction made: {prediction} with confidence: {confidence:.4f}")
            
            return prediction, confidence
            
        except Exception as e:
            logging.error(f"Error making prediction: {str(e)}")
            raise
    
    def save_model(self):
        """Save the trained model and preprocessors"""
        try:
            joblib.dump(self.model, self.model_path)
            joblib.dump(self.label_encoders, self.encoders_path)
            logging.info("Model and preprocessors saved successfully")
        except Exception as e:
            logging.error(f"Error saving model: {str(e)}")
    
    def load_model(self):
        """Load the trained model and preprocessors"""
        try:
            if (os.path.exists(self.model_path) and 
                os.path.exists(self.encoders_path)):
                
                self.model = joblib.load(self.model_path)
                self.label_encoders = joblib.load(self.encoders_path)
                logging.info("Model and preprocessors loaded successfully")
            else:
                logging.info("Model files not found. Will train new model.")
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
