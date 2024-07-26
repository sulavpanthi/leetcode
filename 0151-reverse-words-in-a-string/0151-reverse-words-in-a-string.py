class Solution:
    def reverseWords(self, s: str) -> str:
        
        # using sliding window approach
        result = ""
        p1 = p2 = len(s) - 1
        while p1 >= 0:

            # remove all whitespaces from front
            while s[p2] == " ":
                p2 -= 1

            p1 = p2

            # find the word and append to the result
            while s[p2] != " " and p2 >= 0:
                p2 -= 1
            result = result + " " + s[p2+1:p1+1]

            # remove all whitespaces in between
            while s[p2] == " ":
                p2 -= 1

            p1 = p2

        return result[1:]