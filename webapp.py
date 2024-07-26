import streamlit as st
import functions


st.title("Pig Latin Translator :pig:")
# col1, col2 = st.columns(2)

# with col1:
user_input = st.text_area("What would you like to translate?", placeholder="Enter Text Here")

button_col = st.columns([16, 2.6])
with button_col[1]:
    translate_button = st.button("Translate")

if "text" not in st.session_state:
    st.session_state['text'] = ""

# with col2:
# translated_text_area = st.text_area("", st.session_state['text'],  placeholder="Translation")
translated_text_area = st.code(st.session_state['text'], language="markdown")


translated_sentence = []
vowels = ["A", "E", "I", "O", "U"]
suffix = "ay"

if translate_button:
    for words in user_input.split():
        if words[0].upper() not in vowels and words[1].upper() in vowels:
            translated_word = functions.first_consonant_second_vowel(words)
            translated_sentence.append(translated_word)
        # Checks to see if the first letter is a consonant and the second letter is a vowel
        elif words[0].upper() not in vowels and words[1].upper() not in vowels:
            translated_word = functions.double_consonants(words)
            translated_sentence.append(translated_word)
        # Checks to see if the first letter is a vowel
        elif words[0].upper() in vowels:
            translated_sentence.append(f"{words}w{suffix}")

        translated_sentence[0] = translated_sentence[0].title()

    pig_latin_sentence = " ".join(translated_sentence)
    st.session_state['text'] = pig_latin_sentence
    st.experimental_rerun()

