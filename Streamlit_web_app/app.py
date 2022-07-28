import streamlit as st
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


# make containers
header=st.container()
data_sets=st.container()
features=st.container()
model_training=st.container()

with header:
    st.title('Kashti ki app')
    st.text('In this project we will work on kashti data')

with data_sets:
    st.header('Kashti Doob gayi')
    st.text('We will work with titanic dataset')
    # import data
    df=sns.load_dataset('titanic')
    df=df.dropna()
    st.write(df.head())

    st.subheader('Sambha!!!, Are Ohhh Sambha, kitnay admi thay?')
    st.bar_chart(df['sex'].value_counts())

    #other plots
    st.subheader('Class k hisab se farq')
    st.bar_chart(df['class'].value_counts())
    
    st.bar_chart(df['age'].sample(10))


with features:
    st.header('These are our app features')
    st.text('Awein boht sare features add krte hain, assaan he hai... ')
    st.markdown('1. **Feature 1:** This will tell us pata nhi kiya \ ')
    st.markdown('1. **Feature 2:** This will tell us pata nhi kiya \ ')
    st.markdown('1. **Feature 3:** This will tell us pata nhi kiya \ ')
    st.markdown('1. **Feature 4:** This will tell us pata nhi kiya \ ')


with model_training:
    st.header('Kashti walon ka kiya bana? (model-train)')
    st.text('ye kiya baat hui bhala? hum urdu kese use kr skte hain?')
    # making columns
    input, display = st.columns(2)

    # pehle column main selection points hone chahiye
    max_depth = input.slider('How many people do you know?', min_value=10, max_value=100, value=20, step=5)

#n-estimators
n_estimators=input.selectbox('How many trees should be there in a RF?', options=[50,100,200,300,'NO LIMIT'])

# input features from user

input_feature=input.text_input('Which input we should use?')


# machine learning model
model=RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

#define X and Y

X=df[[input_feature]]
y=df[['fare']]

#fit our model

model.fit(X,y)
pred=model.predict(y)

# Display metrices
display.subheader('Mean absolute error of the model is: ')
display.write(mean_absolute_error)
display.subheader('Mean squared error of the model is: ')
display.write(mean_squared_error)
display.subheader('R Squared score of the model is: ')
display.write(r2_score)


