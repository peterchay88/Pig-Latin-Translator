import streamlit as st
from pig_latin import PigLatin


# Define session States
if "text" not in st.session_state:
    st.session_state['text'] = ""

if "show_translate_text" not in st.session_state:
    st.session_state['show_translate_text'] = False

st.title("Pig Latin Translator :pig:")
# col1, col2 = st.columns(2)

# with col1:
user_input = st.text_area("What would you like to translate?", placeholder="Enter Text Here")

button_col = st.columns([16, 2.6])
with button_col[1]:
    translate_button = st.button("Translate")

# with col2:
translated_text_area = st.text_area("", st.session_state['text'],  placeholder="Translation")


translated_sentence = []
vowels = ["A", "E", "I", "O", "U"]
suffix = "ay"

if translate_button:
    # Trying to get the st.code box to show after clicking the button but rerun() at the bottom refreshes the page
    # rerun is needed in order for the piglatin translator to work. Need to debug it.
    st.session_state['show_translate_text'] = not st.session_state['show_translate_text']
    if st.session_state['show_translate_text']:
        translated_text_area = st.code(st.session_state['text'], language="markdown")
    for words in user_input.split():
        if words[0].upper() not in vowels and words[1].upper() in vowels:
            translated_word = PigLatin().first_consonant_second_vowel(words)
            translated_sentence.append(translated_word)
        # Checks to see if the first letter is a consonant and the second letter is a vowel
        elif words[0].upper() not in vowels and words[1].upper() not in vowels:
            translated_word = PigLatin().double_consonants(words)
            translated_sentence.append(translated_word)
        # Checks to see if the first letter is a vowel
        elif words[0].upper() in vowels:
            translated_sentence.append(f"{words}w{suffix}")

        translated_sentence[0] = translated_sentence[0].title()

    pig_latin_sentence = " ".join(translated_sentence)
    st.session_state['text'] = pig_latin_sentence
    st.rerun()

