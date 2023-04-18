import tkinter as tk
from tkinter import simpledialog
from tkinter.messagebox import showinfo
import functions

vowels = ["A", "E", "I", "O", "U"]
suffix = "ay"

# creating a variable as an empty list to append the translated words to later
translated_sentence = []

application_window = tk.Tk()
user_input = tk.simpledialog.askstring("Pig Latin Translator", "Enter Text Below", parent=application_window)

if user_input is not None:
    user_input = user_input.split(" ")

    for words in user_input:
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
    print(" ".join(translated_sentence))
    showinfo("Translated Sentence",f"{' '.join(translated_sentence)}")