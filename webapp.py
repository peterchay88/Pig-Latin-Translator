import streamlit as st
from pig_latin.pig_latin import PigLatin
from web_page_logic.web_page_logic import translate

# Title
st.title("Pig Latin Translator :pig:")

# User input box & initialize the pig latin class
user_input_field = st.text_area("What would you like to translate?", placeholder="Enter Text Here", key="text")
pig_latin = PigLatin(user_input_field)

# Translate Button
button_col = st.columns([16, 2.6])
with button_col[1]:
    translate_button = st.button("Translate", on_click=translate, key="Translate")

# Translated text area, if translate button is clicked show field and run translate sentence method
if st.session_state['show_translate_text']:
    translated_text_area = st.code(pig_latin.translate_sentence(), language="markdown")




