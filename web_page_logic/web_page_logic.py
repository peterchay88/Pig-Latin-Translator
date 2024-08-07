import streamlit as st


def define_session_states():
    """
    Define session States
    :return:
    """
    if 'show_translate_text' not in st.session_state:
        st.session_state['show_translate_text'] = False
    if 'translate' not in st.session_state:
        st.session_state['translate'] = True
    if 'clear' not in st.session_state:
        st.session_state['clear'] = False
    if 'error' not in st.session_state:
        st.session_state['error'] = False


def translate():
    """
    This function updates the page layout when the user clicks the translate button  on the page by altering the
    session state.
    :return:
    """
    # Show translated text field:
    if st.session_state['text'] != "":
        st.session_state['show_translate_text'] = True
        st.session_state['translate'] = False
        st.session_state['clear'] = True
        st.balloons()
        st.toast("Sentence Translated!", icon="🔥")
        st.session_state['error'] = False
    elif st.session_state['text'] == "":
        st.session_state['error'] = True


def clear():
    """
    This function clears the translated text section and returns the page to its original state
    :return:
    """
    st.session_state['show_translate_text'] = False
    st.session_state['translate'] = True
    st.session_state['clear'] = False
    st.session_state['text'] = ""
    st.toast("Translation Cleared!", icon="🫡")


def footer(text: str, version: float):
    """
    Footer for the web page
    :param text: Footer text
    :param version: app version
    :return:
    """
    i = 0
    while True:
        if i < 12:
            st.write("\n")
            i += 1
        elif i >= 12:
            break
    st.write(f"{text} Version {version}.")