# Problem Statement:
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer
# range [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers.
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    """
    Solves the Reverse Integer problem.
    """
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a signed 32-bit integer.

        This solution reverses the integer by repeatedly taking the last digit
        and appending it to a `reversed_num`. The sign of the original number
        is handled separately.

        The main challenge is handling potential integer overflow. A 32-bit signed
        integer has a range from -2^31 to 2^31 - 1. We must check if the
        `reversed_num` exceeds these bounds at each step of the process.

        - `sign`: Stores the sign of the input `x`.
        - `reversed_num`: Builds the reversed number.
        - `abs_x`: The absolute value of `x` to simplify the reversal loop.

        The overflow check is done by comparing `reversed_num` against the
        maximum possible value (`2**31 - 1`) divided by 10. If `reversed_num`
        is greater than this value, any further addition will cause an overflow.
        There's also a special case to check if `reversed_num` is exactly equal
        to this value and the next digit is greater than 7.

        Args:
            x: A 32-bit signed integer.

        Returns:
            The reversed integer, or 0 if the result overflows.
        """
        # Define the 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        reversed_num = 0
        
        # Handle the sign of the number
        sign = -1 if x < 0 else 1
        abs_x = abs(x)

        while abs_x != 0:
            # Get the last digit
            digit = abs_x % 10
            
            # Check for potential overflow before modifying reversed_num
            # If reversed_num > INT_MAX / 10, then reversed_num * 10 will overflow.
            # If reversed_num == INT_MAX / 10, then it overflows if digit > 7.
            # (since INT_MAX is 2147483647)
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0

            # Append the digit to the reversed number
            reversed_num = reversed_num * 10 + digit
            
            # Remove the last digit from abs_x
            abs_x //= 10
            
        return sign * reversed_num

# Complexity Analysis:
#
# Time Complexity: O(log10(x))
# The number of iterations in the while loop is proportional to the number of
# digits in the integer `x`. The number of digits in `x` is approximately log10(x).
#
# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space to store a few variables,
# regardless of the size of the input integer.
