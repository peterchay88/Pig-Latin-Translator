import streamlit as st

st.set_page_config(layout="wide")
st.title("Pig Latin Translator")
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_input("What would you like to translate?", placeholder="Enter Text Here")

with col2:
    translated_text = st.text_input("", placeholder="Translation")
    st.write("") # add a blank line for spacing
    button_col = st.columns(2)
    with button_col[0]:
        translate_button = st.button("Translate", key="Translate", help="Click to translate the text", margin=(0, 5, 0, 0))
    with button_col[1]:
        clear_button = st.button("Clear", key="Clear", help="Click to clear the input and output fields", margin=(0, 0, 0, 5))
        st.write("") # add a blank line for spacing