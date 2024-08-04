import streamlit as st
from pig_latin.pig_latin import PigLatin


# Define session States
if "text" not in st.session_state:
    st.session_state['text'] = ""

if "show_translate_text" not in st.session_state:
    st.session_state['show_translate_text'] = False

# Title
st.title("Pig Latin Translator :pig:")

# User input box & initialize the pig latin class
user_input = st.text_area("What would you like to translate?", placeholder="Enter Text Here")
pig_latin = PigLatin(user_input)

# Translate Button
button_col = st.columns([16, 2.6])
with button_col[1]:
    translate_button = st.button("Translate")

# Translated text area
translated_text_area = st.text_area("", st.session_state['text'],  placeholder="Translation")

if translate_button:
    # Trying to get the st.code box to show after clicking the button but rerun() at the bottom refreshes the page
    # rerun is needed in order for the piglatin translator to work. Need to debug it.
    st.session_state['show_translate_text'] = not st.session_state['show_translate_text']
    if st.session_state['show_translate_text']:
        translated_text_area = st.code(st.session_state['text'], language="markdown")
    pig_latin_sentence = pig_latin.translate_sentence()

    st.session_state['text'] = pig_latin_sentence
    st.rerun()

