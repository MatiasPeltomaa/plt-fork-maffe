import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_init_and_get_phrase(self):
        phrase = "hello world"
        plt = PigLatin(phrase)
        self.assertEqual(plt.get_phrase(), phrase)

    def test_empty_phrase(self):
        plt = PigLatin("")
        self.assertEqual(plt.translate(), "nil")

    def test_translate_word_start_vowel_end_y(self):
        plt = PigLatin("any")
        self.assertEqual(plt.translate_word("any"), "anynay")

    def test_translate_word_start_vowel_end_vowel(self):
        plt = PigLatin("apple")
        self.assertEqual(plt.translate_word("apple"), "appleyay")

    def test_translate_word_start_vowel_end_consonant(self):
        plt = PigLatin("ask")
        self.assertEqual(plt.translate_word("ask"), "askay")

    def test_translate_word_start_consonant(self):
        plt = PigLatin("yellow")
        self.assertEqual(plt.translate_word("yellow"), "ellowyay")
