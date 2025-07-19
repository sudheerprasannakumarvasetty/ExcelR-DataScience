# app.py

import streamlit as st
import joblib
import numpy as np
model = joblib.load('logistic_model.pkl')
st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details to predict survival:")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ['male', 'female'])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Number of Siblings/Spouse Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.number_input("Fare Paid", 0.0, 600.0, 50.0)
embarked = st.selectbox("Port of Embarkation", ['C', 'Q', 'S'])

sex = 1 if sex == 'male' else 0
embarked_Q = 1 if embarked == 'Q' else 0
embarked_S = 1 if embarked == 'S' else 0

if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked_Q, embarked_S]])
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"The passenger would survive (Probability: {prob:.2f})")
    else:
        st.error(f"The passenger would NOT survive (Probability: {prob:.2f})")
