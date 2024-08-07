import streamlit as st
from pig_latin.pig_latin import PigLatin
from web_page_logic.web_page_logic import translate, clear, define_session_states, footer

define_session_states()

# Title
st.title("Pig Latin Translator :pig:")

# User input box & initialize the pig latin class
user_input_field = st.text_area("What would you like to translate?", placeholder="Enter Text Here", key="text")
pig_latin = PigLatin(user_input_field)

# Translate Button
if st.session_state['translate']:
    button_col = st.columns([16, 2.6])
    with button_col[1]:
        translate_button = st.button("Translate", on_click=translate)
# Clear button
elif st.session_state['clear']:
    button_col = st.columns([20, 2.2])
    with button_col[1]:
        clear_button = st.button("Clear", on_click=clear)

# Translated text area, if translate button is clicked show field and run translate sentence method
if st.session_state['show_translate_text']:
    translated_text_area = st.code(pig_latin.translate_sentence(), language="markdown")
if st.session_state['error']:
    st.error("Error! Please enter something to translate.")

footer(text="This app was built by [Peter Chay.](%s)" % "https://github.com/peterchay88",
       version=1.0)
