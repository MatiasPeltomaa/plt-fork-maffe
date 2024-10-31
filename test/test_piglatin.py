import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_init_and_get_phrase(self):
        phrase = "hello world"
        plt = PigLatin(phrase)
        self.assertEqual(plt.get_phrase(), phrase)
