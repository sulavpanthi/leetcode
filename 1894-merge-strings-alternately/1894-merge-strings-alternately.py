class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        self.merged_string = ""
        self.word1 = word1
        self.word2 = word2
        length_of_word1 = len(word1)
        length_of_word2 = len(word2)

        if length_of_word1 < length_of_word2:
            self.mergeSameLengthStrings(length_of_word1)
            self.merged_string += word2[length_of_word1:]

        elif length_of_word2 < length_of_word1:
            self.mergeSameLengthStrings(length_of_word2)
            self.merged_string += word1[length_of_word2:]

        else:
            self.mergeSameLengthStrings(length_of_word1)

        return self.merged_string

    def mergeSameLengthStrings(self, length):
        for index in range(length):
            self.merged_string += self.word1[index] + self.word2[index]