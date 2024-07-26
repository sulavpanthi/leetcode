class Solution:

    # # Approach 1: Brute force (Generating all subsequences)

    # def substring(self, s, i, res):
    #     if i == len(s):
    #         # to filter out the empty substring
    #         if len(res) > 0:
    #             self.result.append(int("".join(list(res))))
    #         return
    #     res.append(s[i])
    #     self.substring(s, i+1, res)
    #     # use .pop() here to ensure that last added element is removed
    #     # while using .remove() might remove another element instead of recently added element e.g in case of duplicate elements already in the array
    #     res.pop()
    #     # res.remove(s[i])
    #     self.substring(s, i+1, res)

    # def largestOddNumber(self, num: str) -> str:
    #     self.result = []
    #     self.substring(num, 0, [])

    #     # Filter all odd numbers
    #     odd_ones = [x for x in self.result if x % 2 == 1]
    #     if not odd_ones:
    #         return ""

    #     return str(max(odd_ones))




    # Approach 2: Optimal

    def largestOddNumber(self, num: str) -> str:
        largest = ""
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                largest = num[:i+1]
        return largest
