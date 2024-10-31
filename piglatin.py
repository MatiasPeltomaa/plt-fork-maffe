from error import PigLatinError
import re

class PigLatin:
    ALLOWED_PUNCTUATION = {'.', ',', ';', ':', "'", '?', '!', '(', ')'}

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"

        for char in self.phrase:
            if char not in self.ALLOWED_PUNCTUATION and not char.isalnum() and not char.isspace() and char != '-':
                raise PigLatinError(f"Invalid character '{char}' in input phrase.")

        words = self.phrase.split()
        pig_latin_words = []

        for word in words:
            base_word = re.sub(r'[.,;:\'?!()]+$', '', word)
            punctuation = word[len(base_word):]
            parts = base_word.split('-')
            translated_parts = [self.translate_word(part) for part in parts]
            pig_latin_words.append('-'.join(translated_parts) + punctuation)

        return ' '.join(pig_latin_words)

    def translate_word(self, word: str) -> str:
        vowels = "aeiouAEIOU"

        if word[0] in vowels:
            if word[-1] == "y":
                return word + "nay"
            elif word[-1] in vowels:
                return word + "yay"
            else:
                return word + "ay"

        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    return word[i:] + word[:i] + "ay"
            return word + "ay"
