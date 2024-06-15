class Solution:

    def addStrings(self, num1: str, num2: str, carry = 0) -> str:
        if not num1 and not num2:
            return str(carry) if carry > 0 else ""
        if not num1 and carry == 0:
            return num2
        if not num2 and carry == 0:
            return num1
        num1, num2 = num1 or "0", num2 or "0"
        temp_sum = int(num1[-1]) + int(num2[-1]) + carry
        remainder = temp_sum % 10
        carry = temp_sum // 10
        return self.addStrings(num1[:-1], num2[:-1], carry) + str(remainder)