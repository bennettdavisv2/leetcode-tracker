# Last updated: 7/29/2026, 10:14:02 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a mapping of Roman numeral symbols to their values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            current_value = roman_map[s[i]]
            # If the next symbol is larger, subtract the current value
            if i + 1 < len(s) and roman_map[s[i + 1]] > current_value:
                result -= current_value
            else:
                result += current_value

        return result
