import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from scipy.stats import zscore

from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def test(age: int, gender: str, weight: float, height: float, max_bpm: int, avg_bpm: int, resting_bpm: int, session_duration: float, calories_burned: float, workout_type: str, water_intake: float, workout_frequency: int, experience_level: int,bmi :float) -> float:
    columns = ['Age', 'Gender', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM',
       'Resting_BPM', 'Session_Duration (hours)', 'Calories_Burned',
       'Workout_Type', 'Water_Intake (liters)',
       'Workout_Frequency (days/week)', 'Experience_Level', 'BMI']
    data = [age,gender,weight,height,max_bpm,avg_bpm,resting_bpm,session_duration,calories_burned,workout_type,water_intake,workout_frequency,experience_level,bmi]
    X_test = pd.DataFrame([data], columns=columns)
    model = joblib.load('model/best_model.pkl')
    encoder = joblib.load('model/workout_type_encoder.pkl')
    scaler = joblib.load('model/minmax_scaler.pkl')

    X_test['Gender'] = X_test['Gender'].map({'Female': 0, 'Male': 1})
    test_encodings = encoder.transform(X_test[['Workout_Type']])
    test_encodings_df = pd.DataFrame(
        test_encodings,
        columns=encoder.get_feature_names_out(['Workout_Type']),
        index=X_test.index
    )
    X_test = pd.concat([X_test.drop('Workout_Type', axis=1), test_encodings_df], axis=1)
    
    X_test_scaled = scaler.transform(X_test)
    X_test = pd.DataFrame(
        X_test_scaled,
        columns=X_test.columns,   # Preserve column names
        index=X_test.index        # Preserve index
    )
    features_to_drop = ['Session_Duration (hours)', 'Workout_Frequency (days/week)']
    X_test = X_test.drop(columns=features_to_drop, axis=1)

    y_pred = model.predict(X_test)
    return y_pred[0]
    