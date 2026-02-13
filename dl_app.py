
import streamlit as st
import pandas as pd
import tensorflow as tf

# Load the trained DL model
model = tf.keras.models.load_model('deep_learning_model.keras')

st.set_page_config(layout="wide")
st.title('Diabetes Prediction (Deep Learning Model)')

st.write("### Enter Patient Information:")

# Define input fields for the 8 features
with st.form("prediction_form"):
    pregnancies = st.slider('Pregnancies', 0, 17, 3)
    glucose = st.slider('Glucose', 44, 199, 117)  # Median from pre-imputation
    blood_pressure = st.slider('Blood Pressure', 24, 122, 72)  # Median from pre-imputation
    skin_thickness = st.slider('Skin Thickness', 7, 99, 29)  # Median from pre-imputation
    insulin = st.slider('Insulin', 14, 846, 125)  # Median from pre-imputation
    bmi = st.slider('BMI', 18.2, 67.1, 32.3)  # Median from pre-imputation
    diabetes_pedigree_function = st.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725)
    age = st.slider('Age', 21, 81, 29)

    submitted = st.form_submit_button("Predict")

    if submitted:
        # Create a DataFrame from the inputs
        input_data = pd.DataFrame([{
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': diabetes_pedigree_function,
            'Age': age
        }])

        # Make prediction (no scaling needed for this DL model)
        prediction_proba = model.predict(input_data)[0][0]
        prediction = (prediction_proba > 0.5).astype(int)

        st.write("### Prediction Result:")
        if prediction == 1:
            st.error(f"The model predicts diabetes with a probability of {prediction_proba:.2f}")
        else:
            st.success(f"The model predicts no diabetes with a probability of {1 - prediction_proba:.2f}")
