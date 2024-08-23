import streamlit as st
import numpy as np
import nbformat
from nbconvert import PythonExporter

# Load the notebook
with open("Diabetes_file.ipynb") as f:
    notebook = nbformat.read(f, as_version=4)

# Export notebook to Python code
exporter = PythonExporter()
source_code, _ = exporter.from_notebook_node(notebook)

# Execute the code
exec(source_code)


st.set_page_config(page_title = "Know Whether you are Diabetic or Not", layout= 'wide')
st.title(':red[Know whether you are Diabetic or Not]')

name= st.text_input("**Enter your Full name**")
gen=st.selectbox("**Select your Gender**", ('Male','Female','Others'), key = 'gender')
if gen == 'Male':
    gen = 1
elif gen == 'Female':
    gen = 0
elif gen == 'others':
    gen = 2

age = st.text_input("**Enter the Age**")
hypertension = st.selectbox("**Enter Hypertension Status [Blood Pressure]**", ('Yes','No'), key = 'hypertension')
if hypertension == 'Yes':
    hypertension = 1
else:
    hypertension = 0

smoking_history = st.selectbox('**Select smoking_history**', ('never', 'No Info', 'current', 'former', 'ever', 'not current'), key= 'smoking_history ')
if smoking_history == 'never':
    smoking_history = 4
if smoking_history == 'No Info':
    smoking_history = 0
if smoking_history == 'current':
    smoking_history = 1
if smoking_history == 'former':
    smoking_history = 3
if smoking_history == 'ever':
    smoking_history = 2
if smoking_history == 'not current':
    smoking_history = 5

heart_disease =st.selectbox("**Select heart_disease status**",('Yes','No'), key='heart_disease')
if heart_disease =='Yes':
    heart_disease=0
else:
    heart_disease=1

bmi=st.text_input("**Enter your BMI**")
HbA1c_level = st.text_input("***Enter your HbA1c_level**")
blood_glucose_level = st.text_input("**Enter your blood_glucose_level**")

Get_data= st.button("**Retrieve and get results**")

#Define Session state to Get data button
if "Get_state" not in st.session_state:
    st.session_state.Get_state = False
if Get_data or st.session_state.Get_state:
    st.session_state.Get_state = True

    input=np.array([[age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, gen, smoking_history ]])
    input_pred=model.predict(input)
    if input_pred==1:
        st.header(f'''OOPS! {name} You have Diabetes''')
    else:
        st.header(f'''Congrats! {name} You Don't have Diabetes''' )