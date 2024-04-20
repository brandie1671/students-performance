import pandas as pd
import joblib
import streamlit as st

# Load the saved model
model = joblib.load('converted_model.joblib')

# Define a helper function for the radio buttons
def parse_radio(label, options, default):
    selected = st.sidebar.radio(label, tuple(options), key=default)
    return dict(zip(options, [0]*len(options)))[selected]

# Define a helper function for the slider
def parse_slider(label, lower, upper, step):
    return st.sidebar.slider(label, lower, upper, step, key=label)

# Get user input
st.set_page_config(page_title="Model Predictor", page_icon="🔮")
st.title("Student Performance Predictor App")
st.subheader("Please enter the required data:")

Gender = parse_radio("Gender", ("Male", "Female"), "Gender")
Race = parse_radio("Race/ethnicity", ("Group A", "Group B", "Group C", "Group D", "Other"), "Race/ethnicity")
Parental_Level_of_Education = parse_radio("Parental Level of Education",
                                ("some high school", "high school", "associate's degree", "master's degree", "some college", "doctorate degree"),
                                "Parental Level of Education")
Lunch = parse_radio("Lunch", ("standard", "free/reduced"), "Lunch")
test_preparation_course = parse_radio("Test Preparation Course", ("None", "Yes"), "test_preparation_course")

Math_score = parse_slider("Year one Score", 1, 100, 1)
Reading_score = parse_slider("Year two Score", 1, 100, 1)
Writing_score = parse_slider("Year three Score", 1, 100, 1)

user_inputs = [[Gender, Race, Parental_Level_of_Education, Math_score, Reading_score, Writing_score, Lunch, test_preparation_course]]

# Create a prediction button
if st.button('Generate Prediction'):
    # Generate a prediction
    prediction = round(model.predict(user_inputs)[0], 2)
    st.balloons()
    # Show the result
    st.subheader("Prediction")
    st.write(f"The predicted average score is: {prediction}")
else:
    st.write("Click the button to start the prediction process.")