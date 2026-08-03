class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        roman = ""
        decimalPlace = len(s)
        for ch in s:
            d = int(ch)
            if d not in (4, 9):
                if decimalPlace == 4:
                    roman += "M" * d
                if decimalPlace == 3:
                    if d <= 3:
                        roman += "C" * d
                    if d == 5:
                        roman += "D"
                    if d >= 6:
                        roman += "D" + ("C" * (d % 5))
                if decimalPlace == 2:
                    if d <= 3:
                        roman += "X" * d
                    if d == 5:
                        roman += "L"
                    if d >= 6:
                        roman += "L" + ("X" * (d % 5))
                if decimalPlace == 1:
                    if d <= 3:
                        roman += "I" * d
                    if d == 5:
                        roman += "V"
                    if d >= 6:
                        roman += "V" + ("I" * (d % 5))
            else:
                if decimalPlace == 3:
                    roman += "CD" if d == 4 else "CM"
                if decimalPlace == 2:
                    roman += "XL" if d == 4 else "XC"
                if decimalPlace == 1:
                    roman += "IV" if d == 4 else "IX"
            decimalPlace -= 1
        return roman