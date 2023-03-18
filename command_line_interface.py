vowels = ["A", "E", "I", "O", "U"]
suffix = "ay"

user_input = input("What would you like to translate? ")

# creating an if loop that checks if the first letter and second of the user input is a consonant
if user_input[0].upper() not in vowels and user_input[1].upper() in vowels:
    user_input = list(user_input)
    first_letter = user_input[0]
    user_input.pop(0)
    user_input.append(first_letter)
    translated_word = "".join(user_input)
    print(f"{translated_word.title()}{suffix}")

# Checks to see if the first letter is a consonant and the second letter is a vowel
elif user_input[0].upper() not in vowels and user_input[1].upper() not in vowels:
    user_input = list(user_input)
    first_letter = user_input[0]
    second_letter = user_input[1]
    user_input.pop(0)
    user_input.pop(0)
    user_input.extend([first_letter, second_letter])
    translated_word = "".join(user_input)
    print(f"{translated_word.title()}{suffix}")

# Checks to see if the first letter is a vowel
elif user_input[0].upper() in vowels:
    print(f"{user_input.title()}w{suffix}")
