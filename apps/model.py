import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


def app():
    # load models
    saved_tree_clf = joblib.load('clf-best.pickle')
        
    st.title('Model')

    st.write('This is the Model page')

    st.write('The model performance of the Bank Model dataset is presented below.')

    # Load dataset
    df = pd.read_csv('projectdataset-1.csv')

    # Model building
    st.header('Model Performance')
    st.subheader('Making Prediction')
    st.markdown('**Please Provide Information**:')        


    #inputs
    Age = st.slider('Age', min_value=18, max_value=100)
    Balance = int(st.number_input('What is your yearly average balance?'))
    Housing = st.radio("Do you have a house loan?",('Yes','No'))
    Contact = st.radio("How were you contacted",("Cellular",'Telephone','Unknown'))
    Day = int(st.number_input("Which day were you contacted on ",1,31,1))
    Month = st.selectbox('Month', ['January','February','March','April','May','June','July','August','September','October','November','December'])
    Duration = int(st.number_input("Enter Duration of call in seconds",00,5000,00))
    pDays = int(st.number_input("Number of days passed after customer was contacted from last campaign",-1,1000,00))
    pOutcome = st.radio("What was the status of the previous marketing campaign?",( "unknown","other","failure","success"))


    # this is how to dynamically change text
    prediction_state = st.markdown('calculating...')

    banker1 = pd.DataFrame(
        {   
        'age' : 64, 
        'balance' : 109, 
        'housing' : 'no',
        'contact' : 'cellular',
        'day' : 23, 
        'month' : 'jun', 
        'duration' : 706,
        'pdays': 225, 
        'poutcome' : ['success']   
       
        }
    )


    banker2 = pd.DataFrame(
        {'age' : [Age], 
        'balance' : [Balance], 
        'housing' : [Housing],
        'contact' : [Contact],
        'day' : [Day], 
        'month' : [Month], 
        'duration' : [Duration],
        'pdays': [pDays], 
        'poutcome' : [pOutcome]   
       
        }
    )


    y_pred = saved_tree_clf.predict(banker2) 

    if y_pred[0] == 2:
        msg = 'This customer is predicted to be: **subscribed**'
        
    else:
        msg = 'This customer is predicted to be: **Not subscribed**'
       

    prediction_state.markdown(msg)

