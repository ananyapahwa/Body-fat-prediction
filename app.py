
import streamlit as st
from test import test  # Import the test function from test.py

# Set the title and description of the app
st.title("Body Fat Percentage Prediction")
st.write("Unlock your fitness insights — predict your body fat percentage in seconds with smart data!")

# Create input fields for all the features
age = st.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
weight = st.number_input("Weight (kg)", min_value=2.0, max_value=200.0, value=70.0, step=0.1)
height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.75, step=0.01)
max_bpm = st.number_input("Max BPM", min_value=50, max_value=300, value=190)
avg_bpm = st.number_input("Average BPM", min_value=40, max_value=300, value=120)
resting_bpm = st.number_input("Resting BPM", min_value=30, max_value=200, value=70)
session_duration = st.number_input("Session Duration (hours)", min_value=0.0, max_value=24.0, value=1.0, step=0.1)
calories_burned = st.number_input("Calories Burned", min_value=0.0, max_value=10000.0, value=300.0, step=1.0)
workout_type = st.selectbox("Workout Type", ["Cardio", "Strength", "Yoga","HIIT"])  # Add options based on your dataset
water_intake = st.number_input("Water Intake (liters)", min_value=0.0, max_value=20.0, value=2.0, step=0.1)
workout_frequency = st.number_input("Workout Frequency (days/week)", min_value=0, max_value=7, value=3)
experience_level = st.number_input("Experience Level (1=Beginner, 3=Advanced)", min_value=1, max_value=3, value=2)
bmi = st.number_input("BMI", min_value=00.0, value=22.0, step=0.1)

# Add a button to make predictions
if st.button("Predict Fat Percentage"):
    # Call the test function to get the prediction
    prediction = test(
        age=age,
        gender=gender,
        weight=weight,
        height=height,
        max_bpm=max_bpm,
        avg_bpm=avg_bpm,
        resting_bpm=resting_bpm,
        session_duration=session_duration,
        calories_burned=calories_burned,
        workout_type=workout_type,
        water_intake=water_intake,
        workout_frequency=workout_frequency,
        experience_level=experience_level,
        bmi=bmi
    )
    # Display the prediction
    st.success(f"The predicted fat percentage is: {prediction:.2f}%")
