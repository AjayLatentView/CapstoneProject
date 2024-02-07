import pickle
import streamlit as st
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from risk_factor import helper

st.set_page_config(
    page_title="Diabetes Classification",
    page_icon="🤖",
    # layout="wide",
    # initial_sidebar_state="expanded"
)
hidden = '''
<style>
    #MainMenu {visibility:hidden;}
    header {visibility:hidden;}
    footer {visibility:hidden;}
</style>
'''
st.markdown(hidden, unsafe_allow_html=True)


with st.container():

    st.header("Diabetes Classification")
    col1,col2=st.columns(2)

    with col1:
        age = st.text_input("Age",key="age")
        hba1c_level = st.text_input("HbA1C Level", key="hba1c_level")
        blood_glucose_level = st.text_input("Blood Glucose Level", key="blood_glucose_level")
        st.write(age)
    with col2:
        bmi = st.text_input("BMI",key="bmi")
        hypertension = st.selectbox("Hypertension",("yes","no"))
        heart_disease = st.selectbox("Heart Disease",("yes","no"),placeholder = "Yes/No")


    binary = lambda x: 1 if x=="yes" else 0

    hypertension  = binary(hypertension)
    heart_disease = binary(heart_disease)


with open("models\svc.pkl",'rb') as file:
    clf = pickle.load(file)



if st.button("predict"):
    risk = helper([float(hba1c_level),float(blood_glucose_level)])
    str = f"your risk factor is {risk}"
    st.write(str)
    xtest = [age,hba1c_level,blood_glucose_level,bmi,hypertension,heart_disease,risk]
    xtest =np.array([xtest])
    result = clf.predict(xtest)
    st.write(result)
