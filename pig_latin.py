class PigLatin:

    def __init__(self, sentence):
        self.suffix = "ay"
        self.vowels = ["A", "E", "I", "O", "U"]
        self.sentence = sentence

    def first_consonant_second_vowel(self, word):
        translated_words = []
        for letter in word.split():
            letter = list(letter)
            first_letter = letter[0]
            letter.pop(0)
            letter.append(first_letter)
            translated_word = "".join(letter)
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

    def translate_sentence(self):
        translated_sentence = []
        for words in self.sentence.split():
            if words[0].upper() not in self.vowels and words[1].upper() in self.vowels:
                translated_word = self.first_consonant_second_vowel(words)
                translated_sentence.append(translated_word)
            # Checks to see if the first letter is a consonant and the second letter is a vowel
            elif words[0].upper() not in self.vowels and words[1].upper() not in self.vowels:
                translated_word = self.double_consonants()
                translated_sentence.append(translated_word)
            # Checks to see if the first letter is a vowel
            elif words[0].upper() in self.vowels:
                translated_sentence.append(f"{words}w{self.suffix}")
            translated_sentence[0] = translated_sentence[0].title()
        pig_latin_sentence = " ".join(translated_sentence)
        return pig_latin_sentence



