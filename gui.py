import tkinter as tk
import functions

vowels = ["A", "E", "I", "O", "U"]
suffix = "ay"

# creating a variable as an empty list to append the translated words to later
translated_sentence = []


def get_text():
    text = text_field.get('1.0', 'end-1c')
    text = text.split(" ")
    translated_sentence = []

    for words in text:
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

    # Updating the text box where the translated text will go
    pig_latin_sentence = " ".join(translated_sentence)
    translated_text.delete("1.0", tk.END)
    translated_text.insert(tk.END, pig_latin_sentence)


def clear_text():
    translated_text.delete("1.0", tk.END)
    text_field.delete("1.0", tk.END)


# creating the window for the GUI
application_window = tk.Tk()
application_window.title("Pig Latin Translator")
application_window.geometry("600x100")

# creating the label for the GUI
label = tk.Label(application_window, text="What would you like to translate?")
label.place(x=10, y=1)

label2 = tk.Label(application_window, text="Translated Text:")
label2.place(x=300, y=1)

# creating a text field for the user to input what needs to be translated
text_field = tk.Text(application_window, width=40, height=3)
text_field.place(x=10, y=20)

# creating buttons for the GUI
translate_button = tk.Button(application_window, text="Translate", padx=15, command=get_text)
translate_button.place(x=362, y=64)

clear_button = tk.Button(application_window, text="Clear", padx=20, command=clear_text)
clear_button.place(x=482, y=64)

# Creating the text field where the translated text will appear
translated_text = tk.Text(application_window, width=40, height=3)
translated_text.place(x=300, y=20)

application_window.mainloop()

