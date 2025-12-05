"""
Converts a non-negative integer into its full English words representation.

Time Complexity: O(log10(n))
Space Complexity: O(log10(n))

Approach (brief):
We split the number into 3-digit groups (thousands, millions, etc.).  
Each 3-digit chunk is converted using a helper that handles numbers <20, tens, and hundreds.  
We then append the appropriate scale word (Thousand, Million, Billion) to each chunk and build the final string.
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        less_than_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def convert(num):
            if num == 0:
                return ""
            if num < 20:
                return less_than_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + convert(num % 10)
            else:
                return less_than_20[num // 100] + " Hundred " + convert(num % 100)

        i = 0
        res = ""

        while num:
            temp = num % 1000
            if temp:
                res = convert(temp) + thousands[i] + " " + res
            i += 1
            num //= 1000

        return res.strip()
