class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Sort the original word for comparison
        sorted_word = sorted(self.word)

        # Return all words that are true anagrams (excluding identical words)
        return [
            candidate for candidate in word_list
            if sorted(candidate.lower()) == sorted_word and candidate.lower() != self.word
        ]
