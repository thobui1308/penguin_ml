import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
st.title('Penguin Classifier: A Machine Learning App')
st.write("This app uses 6 inputs to predict the species of penguin using "
 "a model built on the Palmer Penguins dataset. Use the form below"
 " to get started!")
password_guess = st.text_input('What is the Password?')
if password_guess != 'streamlit_password':
 st.stop()
penguin_file = st.file_uploader('Upload your own penguin data')
