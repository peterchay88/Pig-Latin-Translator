vowels = ["A", "E", "I", "O", "U"]
suffix = "ay"


def first_consonant_second_vowel(user_input_local):
    english_word = list(user_input_local)
    first_letter = english_word[0]
    english_word.pop(0)
    english_word.append(first_letter)
    translated_word = "".join(english_word)
    print(f"{translated_word.title()}{suffix}")


def double_consonants(user_input_local):
    english_word = list(user_input_local)
    first_letter = english_word[0]
    second_letter = english_word[1]
    english_word.pop(0)
    english_word.pop(0)
    english_word.extend([first_letter, second_letter])
    translated_word = "".join(english_word)
    print(f"{translated_word.title()}{suffix}")


user_input = input("What would you like to translate? ")

# creating an if loop that checks if the first letter and second of the user input is a consonant
if user_input[0].upper() not in vowels and user_input[1].upper() in vowels:
    first_consonant_second_vowel(user_input)

# Checks to see if the first letter is a consonant and the second letter is a vowel
elif user_input[0].upper() not in vowels and user_input[1].upper() not in vowels:
    double_consonants(user_input)

# Checks to see if the first letter is a vowel
elif user_input[0].upper() in vowels:
    print(f"{user_input.title()}w{suffix}")

# This is a test
