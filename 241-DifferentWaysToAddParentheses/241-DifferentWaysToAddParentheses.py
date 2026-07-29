# Last updated: 7/29/2026, 10:13:19 AM
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # This dictionary is used for memoization to store results of subproblems
        memo = {}

        def compute(expression):
            # If the expression is already calculated, return the stored result
            if expression in memo:
                return memo[expression]

            results = []
            # Try to split the expression at each operator
            for i, char in enumerate(expression):
                if char in ['+', '-', '*']:
                    # Recursively solve for the left and right parts
                    left_results = compute(expression[:i])
                    right_results = compute(expression[i+1:])

                    # Combine results of left and right parts
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)

            # If the expression is a number, just return it
            if not results:
                results.append(int(expression))

            # Store the result in memo
            memo[expression] = results
            return results

        return compute(expression)