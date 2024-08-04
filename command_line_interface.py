from pig_latin import PigLatin

user_input = input("What would you like to translate? ")
pig_latin = PigLatin(user_input)
pig_latin_word = pig_latin.translate_sentence()

print(pig_latin_word)