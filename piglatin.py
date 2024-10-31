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
            if len(word) > 1 and word[0] not in vowels:
                return word[1:] + word[0] + "ay"
            else:
                return word + "ay"
