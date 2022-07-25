import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns

#web app ka title

st.markdown('''
 # **Exploratory Data Analysis Web application**
 This app is developed by Furqan Ahmed.
''')

# How to upload file from local machine

with st.sidebar.header('Upload your dataset (.csv)'):
    uploaded_file = st.sidebar.file_uploader("Upload your dataset (.csv)", type=["csv"])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)")

# profiling report for pandas

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df=load_csv()
    pr=ProfileReport(df, explorative=True)
    st.header('***Input DF***')
    st.write(df)
    st.write('---')
    st.header('***Profile Report with Pandas***')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded')
    if st.button('Press to use example data'):
        #example dataset
        def load_data():
            a = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')
            return a
        df=load_data()
        pr=ProfileReport(df, explorative=True)
        st.header('***Input DF***')
        st.write(df)
        st.write('---')
        st.header('***Profile Report with Pandas***')
        st_profile_report(pr)