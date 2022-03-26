#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Tips_Dataset")
#import dataset
df = pd.read_csv('tips.csv')
#First thirty rows
tips = df.head(10)
#Display the table
st.table(tips)
st.header("Visualisation Using Seaborn")
####################################
#bar plot
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()
####################################
#Correation
st.subheader("Heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()
