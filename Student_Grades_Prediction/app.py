import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sidebar with creator's information
st.sidebar.title("About the Creator")
st.sidebar.info("""
Ebenezer Oluwafemi is a dedicated Data Analyst and Data Science enthusiast currently undergoing training with 3MTT in Nigeria.
He developed this tool to help students and parents predict and verify grades, promoting better goal-setting and academic performance.
""")

# Load the trained model and scaler
model = joblib.load('student_grade_predictor.pkl')
scaler = StandardScaler()

# Title of the app
st.title('Student Grade Predictor')
st.subheader("A tool for students and parents to set academic goals and verify school scores")

# Layout for compact design with half-term labels
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### First Half-Term")
    classwork1 = st.number_input('Classwork 1', min_value=0.0, max_value=10.0, step=0.1)
    assignment1 = st.number_input('Assignment 1', min_value=0.0, max_value=10.0, step=0.1)
    classwork2 = st.number_input('Classwork 2', min_value=0.0, max_value=10.0, step=0.1)
    assignment2 = st.number_input('Assignment 2', min_value=0.0, max_value=10.0, step=0.1)
    first_ca = st.number_input('First Continuous Assessment (CA)', min_value=0.0, max_value=10.0, step=0.1)

with col2:
    st.markdown("#### Second Half-Term")
    project = st.number_input('Project', min_value=0.0, max_value=10.0, step=0.1)
    classwork3 = st.number_input('Classwork 3', min_value=0.0, max_value=10.0, step=0.1)
    classwork4 = st.number_input('Assignment 3', min_value=0.0, max_value=10.0, step=0.1)
    second_ca = st.number_input('Second Continuous Assessment (CA)', min_value=0.0, max_value=10.0, step=0.1)
    exam = st.number_input('Exam', min_value=0.0, max_value=100.0, step=0.1)

# Function to map numerical grades to letter grades
def map_grade(numerical_grade):
    if numerical_grade >= 75:
        return 'A1'
    elif numerical_grade >= 70:
        return 'B2'
    elif numerical_grade >= 65:
        return 'B3'
    elif numerical_grade >= 60:
        return 'C4'
    elif numerical_grade >= 55:
        return 'C5'
    elif numerical_grade >= 50:
        return 'C6'
    elif numerical_grade >= 45:
        return 'D7'
    elif numerical_grade >= 40:
        return 'E8'
    else:
        return 'F9'

# Predict button
if st.button('Predict Grade'):
    # Calculate the necessary features
    total40 = round(classwork1 + assignment1 + classwork2 + assignment2, 2)
    actual_score1 = round(total40 / 4, 2)
    half_term_score = round(actual_score1 + first_ca, 2)
    total20 = round((project + second_ca + classwork3 + classwork4) / 2, 2)
    total_ca = round(half_term_score + total20, 2)
    grand_total = round(exam + total_ca, 2)

    # Map the Grand Total to a letter grade
    letter_grade = map_grade(grand_total)

    # Display the prediction
    st.markdown(f"### Predicted Grade: **{letter_grade}**")
    st.write(f"**Grand Total:** {grand_total}")
    
    # Display a data preview if needed for debugging or review
    with st.expander("See calculation details"):
        st.write({
            'Total40': total40,
            'ActualScore': actual_score1,
            'HalfTermScore': half_term_score,
            'Total20': total20,
            'TotalCA': total_ca,
            'Exam': exam,
            'GrandTotal': grand_total
        })
