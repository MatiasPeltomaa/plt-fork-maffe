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

    def test_translate_word_start_single_consonant(self):
        plt = PigLatin("yellow")
        self.assertEqual(plt.translate_word("yellow"), "ellowyay")

    def test_translate_word_start_multiple_consonant(self):
        plt = PigLatin("known")
        self.assertEqual(plt.translate_word("known"), "ownknay")

    def test_translate_multiple_words(self):
        plt = PigLatin("hello world")
        self.assertEqual(plt.translate(), "ellohay orldway")

    def test_translate_composite_words(self):
        plt = PigLatin("well-being")
        self.assertEqual(plt.translate(), "ellway-eingbay")

    def test_translate_mixed_words(self):
        plt = PigLatin("hello well-being world")
        self.assertEqual(plt.translate(), "ellohay ellway-eingbay orldway")

    def test_translate_with_allowed_punctuation(self):
        plt = PigLatin("hello world!")
        self.assertEqual(plt.translate(), "ellohay orldway!")

        plt = PigLatin("well-being, how are you?")
        self.assertEqual(plt.translate(), "ellway-eingbay, owhay areyay ouyay?")

    def test_translate_with_disallowed_punctuation(self):
        with self.assertRaises(PigLatinError):
            plt = PigLatin("hello world#")
            plt.translate()

        with self.assertRaises(PigLatinError):
            plt = PigLatin("hello@world!")
            plt.translate()

    def test_translate_upper_case(self):
        plt = PigLatin("APPLE")
        self.assertEqual(plt.translate(), "APPLEYAY")

    def test_translate_title_case(self):
        plt = PigLatin("Hello")
        self.assertEqual(plt.translate(), "Ellohay")

    def test_translate_invalid_case(self):
        with self.assertRaises(PigLatinError):
            plt = PigLatin("biRd")
            plt.translate()
