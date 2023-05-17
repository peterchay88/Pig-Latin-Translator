import streamlit as st
from st_btn_select import st_btn_select

st.set_page_config(layout="wide")
st.title("Pig Latin Translator")
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area("What would you like to translate?", placeholder="Enter Text Here")

with col2:
    translated_text = st.text_area("", placeholder="Translation")
    button_col = st.columns([2.5, 1])
    with button_col[1]:
        selection = st_btn_select(('Translate', 'Clear'))

