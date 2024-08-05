import streamlit as st

# Define session States
st.session_state['show_translate_text'] = False
st.session_state['translate'] = True
st.session_state['clear'] = False


def translate():
    """
    This function updates the page layout when the user clicks the translate button
    on the page by altering the session state
    :return:
    """
    # Show translated text field:
    st.session_state['show_translate_text'] = True
    st.session_state['translate'] = False
    st.session_state['clear'] = True
