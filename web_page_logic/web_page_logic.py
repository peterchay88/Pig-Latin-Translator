import streamlit as st

# Define session States
st.session_state['show_translate_text'] = False


def translate():
    # Show translated text field:
    st.session_state['show_translate_text'] = True
