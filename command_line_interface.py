# creating a list of consonants from the consonants text file
with open("consonants.txt", "r") as file:
    consonants = file.readlines()
consonants = [item.strip() for item in consonants]

user_input = input("What would you like to translate? ").upper()
suffix = "ay"

# creating an if loop that checks if the first letter of the user input is a consonant
if user_input[0] in consonants:
    user_input = list(user_input)
    first_letter = user_input[0]
    user_input.pop(0)
    user_input.append(first_letter)
    translated_word = "".join(user_input)
    print(f"{translated_word}ay")
