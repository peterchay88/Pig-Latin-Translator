suffix = "ay"
vowels = ["A", "E", "I", "O", "U"]


def first_consonant_second_vowel(user_input_local):
    translated_words = []
    english_words = user_input_local.split(" ")
    for english_word in english_words:
        english_word = list(english_word)
        first_letter = english_word[0]
        english_word.pop(0)
        english_word.append(first_letter)
        translated_word = "".join(english_word)
        translated_words.append(translated_word)
    pig_latin_sentence = " ".join(translated_words)
    return f"{pig_latin_sentence}{suffix}"


def double_consonants(user_input_local):
    english_word = list(user_input_local)
    first_letter = english_word[0]
    second_letter = english_word[1]
    english_word.pop(0)
    english_word.pop(0)
    english_word.extend([first_letter, second_letter])
    translated_word = "".join(english_word)
    return f"{translated_word}{suffix}"
