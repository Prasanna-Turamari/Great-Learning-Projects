
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from xverse.transformer import WOE
from sklearn.ensemble import RandomForestClassifier
import pickle
pipe = pickle.load(open('credit_card_approval.pkl' , 'rb'))

st.title('Credit Card Approval App')
st.subheader('By Mayur Shrotriya')

st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKSiEsPKQAUEEk7kmEy1Rb7YotukM86O286A&usqp=CAU",width=150)
st.sidebar.markdown("[Connect with me on Linkedin!](https://www.linkedin.com/in/mayur-shrotriya-b45133142/)")



c1 , c2, c3 = st.columns(3)


CODE_GENDER = c1.radio('Gender:', ['Male', 'Female'])
CODE_GENDER = 'M' if CODE_GENDER == 'Male' else 'F'

FLAG_OWN_CAR = c2.radio('Own a car?:', ['Yes', 'No'])
FLAG_OWN_CAR = 0 if FLAG_OWN_CAR == 'No' else 1

FLAG_OWN_REALTY = c3.radio('Own a property?:', ['Yes', 'No'])
FLAG_OWN_REALTY = 0 if FLAG_OWN_REALTY == 'No' else 1


c1 , c2 = st.columns(2)
CNT_CHILDREN = c1.number_input('Count of Children :',min_value = 0, max_value = 20)
CNT_FAM_MEMBERS = c2.number_input('Count of Family Members :',min_value = 0, max_value = 20)

AMT_INCOME_TOTAL = c1.number_input('Total Income :')
NAME_INCOME_TYPE = c2.selectbox('Income Type',['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student'])

NAME_EDUCATION_TYPE = c1.selectbox('Education Type :',['Higher education', 'Secondary / secondary special', 'Incomplete higher', 'Lower secondary', 'Academic degree'])
NAME_FAMILY_STATUS = c2.selectbox('Family Status', ['Civil marriage', 'Married', 'Single / not married', 'Separated', 'Widow'])

NAME_HOUSING_TYPE = c1.selectbox('House Type :',['Rented apartment', 'House / apartment', 'Municipal apartment', 'With parents', 'Co-op apartment', 'Office apartment'])
AGE = c2.number_input('Age (In Years)',max_value = 100)
DAYS_BIRTH = - AGE * 365 

WORK_YEARS = c1.number_input('Work Years',max_value = 70)
DAYS_EMPLOYED = - WORK_YEARS / 365
OCCUPATION_TYPE = c2.selectbox('Occupation Type', ['NA', 'Security staff', 'Sales staff', 'Accountants', 'Laborers', 'Managers', 'Drivers', 'Core staff', 'High skill tech staff', 'Cleaning staff', 'Private service staff', 'Cooking staff', 'Low-skill Laborers', 'Medicine staff', 'Secretaries', 'Waiters/barmen staff', 'HR staff', 'Realty agents', 'IT staff'])

FLAG_MOBIL = c1.radio('Own a Mobile?',['Yes','No'])
FLAG_MOBIL = 0 if FLAG_MOBIL == 'No' else 1

FLAG_WORK_PHONE = c2.radio('Own a Work Phone?',['Yes','No'])
FLAG_WORK_PHONE = 0 if FLAG_WORK_PHONE == 'No' else 1

FLAG_PHONE = c1.radio('Own a Phone?',['Yes','No'])
FLAG_PHONE = 0 if FLAG_PHONE == 'No' else 1

FLAG_EMAIL = c2.radio('Own a Email?',['Yes','No'])
FLAG_EMAIL = 0 if FLAG_EMAIL == 'No' else 1



inp = pd.DataFrame([[CODE_GENDER, FLAG_OWN_CAR, FLAG_OWN_REALTY, CNT_CHILDREN, AMT_INCOME_TOTAL, NAME_INCOME_TYPE, NAME_EDUCATION_TYPE, NAME_FAMILY_STATUS, NAME_HOUSING_TYPE, DAYS_BIRTH, DAYS_EMPLOYED, FLAG_MOBIL, FLAG_WORK_PHONE, FLAG_PHONE, FLAG_EMAIL, OCCUPATION_TYPE, CNT_FAM_MEMBERS]],columns=['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 
               'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'FLAG_MOBIL', 
               'FLAG_WORK_PHONE', 'FLAG_PHONE', 'FLAG_EMAIL', 'OCCUPATION_TYPE', 'CNT_FAM_MEMBERS'])
st.write(inp)

pred = pipe.predict(inp)

if pred == 1:
    out = 'Your Credit Card is Approved!'
else:
    out = 'Your Credit Card is Not Approved!'
    
if st.button('Predict Approval for Credit Card'):
    st.success(out)
