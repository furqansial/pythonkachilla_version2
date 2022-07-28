import streamlit as st
import seaborn as sns


st.header('This webapp is brought to you by Furqan Ahmed')
st.text('G I am very exited to learn Data Science')
st.header('par mujhy pata hai kiya likhna hai')

df=sns.load_dataset('iris')

st.write(df[['species', 'sepal_length', 'petal_length']].head(10))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])