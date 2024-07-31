class PigLatin:

    def __init__(self, sentence):
        self.suffix = "ay"
        self.vowels = ["A", "E", "I", "O", "U"]
        self.sentence = sentence

    def first_consonant_second_vowel(self):
        translated_words = []
        english_words = self.sentence.split(" ")
        for english_word in english_words:
            english_word = list(english_word)
            first_letter = english_word[0]
            english_word.pop(0)
            english_word.append(first_letter)
            translated_word = "".join(english_word)
            translated_words.append(translated_word)
        pig_latin_sentence = " ".join(translated_words)
        return f"{pig_latin_sentence}{self.suffix}"

    def double_consonants(self):
        english_word = list(self.sentence)
        first_letter = english_word[0]
        second_letter = english_word[1]
        english_word.pop(0)
        english_word.pop(0)
        english_word.extend([first_letter, second_letter])
        translated_word = "".join(english_word)
        return f"{translated_word}{self.suffix}"

    def translate_word(self):
        translated_sentence = []
        for words in self.sentence:
            if words[0].upper() not in self.vowels and words[1].upper() in self.vowels:
                translated_word = self.first_consonant_second_vowel()
                translated_sentence.append(translated_word)
            # Checks to see if the first letter is a consonant and the second letter is a vowel
            elif words[0].upper() not in self.vowels and words[1].upper() not in self.vowels:
                translated_word = self.double_consonants()
                translated_sentence.append(translated_word)
            # Checks to see if the first letter is a vowel
            elif words[0].upper() in self.vowels:
                translated_sentence.append(f"{words}w{self.suffix}")

    # if words[0].upper() not in vowels and words[1].upper() in vowels:
    #     translated_word = PigLatin().first_consonant_second_vowel(words)
    #     translated_sentence.append(translated_word)
    # # Checks to see if the first letter is a consonant and the second letter is a vowel
    # elif words[0].upper() not in vowels and words[1].upper() not in vowels:
    #     translated_word = PigLatin().double_consonants(words)
    #     translated_sentence.append(translated_word)
    # # Checks to see if the first letter is a vowel
    # elif words[0].upper() in vowels:
    #     translated_sentence.append(f"{words}w{suffix}")

