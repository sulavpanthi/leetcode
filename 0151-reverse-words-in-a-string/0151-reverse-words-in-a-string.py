class Solution:
    def reverseWords(self, s: str) -> str:
        
        # using sliding window approach
        result = []
        p1, p2 = len(s) - 1, len(s) - 1
        while p1 >= 0:
            print("\n\np1 and p2 at start", p1, p2)

            # remove all whitespaces
            while s[p2] == " ":
                p2 -= 1

            p1 = p2

            # find the word and append to the result
            while s[p2] != " " and p2 >= 0:
                p2 -= 1
            result.append(s[p2+1:p1+1])

            print("resutl after append", result, p1, p2)

            # remove all whitespaces
            while s[p2] == " ":
                p2 -= 1

            p1 = p2

            print("p1 and p2 at last", p1, p2)
        return " ".join(result)