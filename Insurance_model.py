# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:08:29 2023

@author: Vedant Gujarathi
"""
import streamlit as st
import numpy as np 
import pickle

Regressor = pickle.load(open('regressor_model.pkl', 'rb'))

def welcome():
    return "WElCOME ALL"

def predict_Insurance_Amount(input_data):
    inputa = np.asarray(input_data)
    samp = inputa.reshape(1,-1) 
    prediction = Regressor.predict(samp)
    return prediction
 

def main():
    
    st.title("Insurance Amount Predictor")
    html_temp ="""
    <div style="background-color:tomato; padding: 10px">
    <h2 style="color:Blue; text-align:center;">Insurance Amount Predictor</h2>
    </div>
    """
    SEX_CHOICES = {0: "female", 1: "male"} 
    REGION_CHOICES = {0:'Southwest',1:'Southeast',2:'Northeast',3:'Northwest'}
    SMOKER_CHOICES = {0:'no',1:'yes'}
    
    
    def format_func1(option):
        return SEX_CHOICES[option]
    
    def format_func2(option):
        return REGION_CHOICES[option]
    
    def format_func3(option):
        return SMOKER_CHOICES[option]
    
    age = st.text_input("age","Type Here")
    sex = st.selectbox("SELECT SEX", options=list(SEX_CHOICES.keys()), format_func=format_func1)
    bmi = st.text_input("bmi","Type Here")
    children = st.text_input("children","Type Here")
    smoker = st.selectbox("SMOKER (YES/NO)", options=list(SMOKER_CHOICES.keys()), format_func=format_func3)
    region = st.selectbox("Select REGION", options=list(REGION_CHOICES.keys()), format_func=format_func2)
    
    result = ""
    if st.button("predict"):
        result = predict_Insurance_Amount([int(age),int(sex),int(bmi),int(children),int(smoker),int(region)])
    st.success('The Output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Created by Vedant Gujarathi")
        
if __name__ == '__main__':
    main()
              
