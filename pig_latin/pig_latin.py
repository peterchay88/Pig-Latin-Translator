class PigLatin:
    __suffix = "ay"
    __vowels = ["A", "E", "I", "O", "U"]

    def __init__(self, sentence: str):
        self.sentence = sentence

    def first_consonant_second_vowel(self, word: str) -> str:
        """
        This method translates words that have the first letter consonant and second letter vowel into pig latin
        :param word: Word to be translated into pig latin
        :return: Translated word
        """
        english_word = [letter for letter in word]
        first_letter = english_word[0]
        english_word.pop(0)
        english_word.append(first_letter)
        translated_word = "".join(english_word)
        return f"{translated_word}{self.__suffix}"

    def double_consonants(self, word: str) -> str:
        """
        This method translated words that start with two consonants into pig latin
        :param word: Word to be translated into pig latin
        :return: Translated word
        """
        english_word = [letter for letter in word]
        first_letter = english_word[0]
        second_letter = english_word[1]
        word_being_translated = english_word[2:]
        word_being_translated.extend([first_letter, second_letter])
        translated_word = "".join(word_being_translated)
        return f"{translated_word}{self.__suffix}"

    def translate_sentence(self) -> str:
        """
        This method takes in the sentence initialized with the object and calls the correct method for translating each
        word to translate it to pig latin
        :return: Translated sentence
        """
        translated_sentence = []
        for words in self.sentence.split():
            if len(words) == 1:
                if words.lower() == 'a' or words.lower() == 'i':
                    translated_sentence.append(words + "yay")
                else:
                    translated_sentence.append(words)
            elif words[0].upper() not in self.__vowels and words[1].upper() in self.__vowels:
                translated_sentence.append(self.first_consonant_second_vowel(words))
            # Checks to see if the first letter is a consonant and the second letter is a vowel
            elif words[0].upper() not in self.__vowels and words[1].upper() not in self.__vowels:
                translated_sentence.append(self.double_consonants(words))
            # Checks to see if the first letter is a vowel
            elif words[0].upper() in self.__vowels:
                translated_sentence.append(f"{words}w{self.__suffix}")
            translated_sentence[0] = translated_sentence[0].title()
        pig_latin_sentence = " ".join(translated_sentence)
        return pig_latin_sentence



