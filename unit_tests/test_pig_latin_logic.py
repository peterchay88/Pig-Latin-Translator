import pytest
from pig_latin import PigLatin


class TestPigLatin:

    @pytest.mark.parametrize("sentence, expected_result", [
        pytest.param("Peter is awesome", "Eterpay isway awesomeway"),
        pytest.param("Pig latin is fun", "Igpay atinlay isway unfay"),
        pytest.param("The curious cat watched the raindrops race down the windowpane",
                     "Ethay uriouscay atcay atchedway ethay aindropsray aceray ownday ethay indowpaneway")
    ])
    def test_sentence_all_string_first_consonant_second_vowel(self, sentence, expected_result):
        """
        This test confirms when we send sentence of only strings through the pig latin translator code
        we get the expected return.

        This test specifically tests words that have its first letter consonant second letter vowel
        :return:
        """
        pl = PigLatin(sentence)
        assert pl.translate_sentence() == expected_result, \
            f"Error unexpected result. Expected: {expected_result}. Actual: {pl.translate_sentence()}"
        pass

    def test_sentence_with_numbers(self):
        """
        This test confirms when we send a sentence of with strings and numbers it is handled as expected.
        :return:
        """
        pass

    def test_sentence_with_punctuations(self):
        """
        This test confirms when we send a sentence of with strings and punctuations it is handled as expected.
        :return:
        """
        pass