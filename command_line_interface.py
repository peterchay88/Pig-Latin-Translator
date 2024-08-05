from pig_latin.pig_latin import PigLatin

print("----------------------------------------")
print("Welcome to the Pig Latin Translator!")
print("---------------------------------------- \n \n")

user_input = input("What would you like to translate?\n")
pig_latin = PigLatin(user_input)
print("\nTranslation:")
print(pig_latin.translate_sentence())