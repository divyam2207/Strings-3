"""
Evaluates a basic arithmetic expression containing +, -, *, / with truncation toward zero.

Time Complexity: O(n)
Space Complexity: O(n)

Approach (brief):
Iterate through the string, building numbers and applying the last seen operator once a full number is parsed.
Use a stack initialized with 1 as a placeholder; push values for +/-, and modify the top for */.
Division uses int(a/b) for truncation toward zero. Final answer is sum(stack) minus the initial placeholder.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        operator = "+"

        i = 0

        while i < len(s):

            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                if operator == "*":
                    stack[-1] *= num
                elif operator == "/":
                    top = stack[-1]
                    temp = int(top / num)  # truncation toward zero
                    stack[-1] = temp
                elif operator == "-":
                    stack.append(-1 * num)
                else:
                    stack.append(num)

                operator = "+"

            elif s[i] in ["+", "-", "*", "/"]:
                operator = s[i]
                i += 1
            else:
                i += 1

        return sum(stack) - 1
