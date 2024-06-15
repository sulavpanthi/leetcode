class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_number = 0
        original_number = x
        while (x>0):
            remainder = x%10
            reverse_number = reverse_number * 10 + remainder
            x //= 10
        if original_number == reverse_number:
            return True
        return False