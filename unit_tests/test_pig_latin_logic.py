import pytest
from pig_latin import PigLatin


class TestPigLatin:

    @pytest.mark.parametrize("sentence, expected_result", [
        pytest.param("brick", "Ickbray"),
        pytest.param("mango", "Angomay"),
        pytest.param("umbrella", "Umbrellaway"),
        pytest.param("Peter is awesome", "Eterpay isway awesomeway"),
        pytest.param("Pig latin is fun", "Igpay atinlay isway unfay"),
        pytest.param("The curious cat watched the raindrops race down the windowpane",
                     "Ethay uriouscay atcay atchedway ethay aindropsray aceray ownday ethay indowpaneway"),
        pytest.param("The golden retriever eagerly chased the bouncing tennis ball across the sunny park",
                     "Ethay oldengay etrieverray eagerlyway asedchay ethay ouncingbay ennistay allbay acrossway ethay "
                     "unnysay arkpay")
    ])
    def test_translate_sentence_string_only(self, sentence, expected_result):
        """
        This test confirms when we send sentence of only strings through the pig latin translator code
        we get the expected return.
        :return:
        """
        pl = PigLatin(sentence)
        assert pl.translate_sentence() == expected_result, \
            f"Error unexpected result. Expected: {expected_result}. Actual: {pl.translate_sentence()}"
        pass

    @pytest.mark.parametrize("word, expected_result", [
        pytest.param("brick", "ickbray"),
        pytest.param("clock", "ockclay"),
        pytest.param("flamethrower", "amethrowerflay"),
        pytest.param("draftbeer", "aftbeerdray")
    ])
    def test_double_consonants(self, word, expected_result):
        """
        This test confirms that words that start with two consonants are translated properly
        :return:
        """
        pl = PigLatin("")
        assert pl.double_consonants(word) == expected_result, \
            f"Error unexpected result. Expected: {expected_result}. Actual: {pl.double_consonants(word)}"

    @pytest.mark.parametrize("word, expected_result", [
        pytest.param("battery", "atterybay"),
        pytest.param("man", "anmay"),
        pytest.param("gemini", "eminigay"),
        pytest.param("network", "etworknay")
    ])
    def test_first_letter_consonant_second_letter_vowel(self, word, expected_result):
        """
        This test confirms that words that start with a consonant and second letter is a vowel  are translated properly
        :return:
        """
        pl = PigLatin("")
        assert pl.first_consonant_second_vowel(word) == expected_result, \
            f"Error unexpected result. Expected: {expected_result}. Actual: {pl.first_consonant_second_vowel(word)}"

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
