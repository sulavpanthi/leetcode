class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        final_val = 0
        previous_symbol = None
        current_symbol = None
        for val in s[::-1]:
            if previous_symbol and val == "I" and previous_symbol in ["V", "X"]:
                final_val -= 1
            elif previous_symbol and val == "X" and previous_symbol in ["L", "C"]:
                final_val -= 10
            elif previous_symbol and val == "C" and previous_symbol in ["D", "M"]:
                final_val -= 100
            else:
                final_val += symbol_values[val]
            previous_symbol = val
        return final_val