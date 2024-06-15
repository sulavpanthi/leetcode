class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        array_length = len(s)
        for i in range(array_length // 2):
            temp = s[i]
            s[i] = s[array_length - 1 - i]
            s[array_length - 1 - i] = temp


        