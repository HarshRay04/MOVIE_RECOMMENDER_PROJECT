import streamlit as st
from click import option

st.title('movie recommender system')

option = st.selectbox(
    'the movie you want to see',
    ('movie1','movie2')
)