class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"

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
                    return word[i:] + word [:i] + "ay"
            return word + "ay"
