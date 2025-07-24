# LeetCode Problem 3: Longest Substring Without Repeating Characters
#
# Problem Statement:
# Given a string `s`, find the length of the longest substring without
# repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    """
    Solves the Longest Substring Without Repeating Characters problem.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        This solution uses the "sliding window" technique. A window is a
        substring of `s`, and we try to expand this window as much as possible
        to the right, and when we find a repeating character, we shrink the
        window from the left.

        A hash map (dictionary in Python) is used to store the most recent
        index of each character we have encountered.

        - `start`: The starting index of the current non-repeating substring.
        - `max_length`: The maximum length found so far.
        - `char_map`: A dictionary to store `character -> last seen index`.

        When we encounter a character that is already in our map and its index
        is within our current window (i.e., its index is >= start), we update
        the start of our window to be the index right after the last occurrence
        of that character.

        Args:
            s: The input string.

        Returns:
            The length of the longest substring without repeating characters.
        """
        # Dictionary to store the last seen index of each character.
        char_map = {}
        max_length = 0
        # `start` is the starting index of the current window.
        start = 0

        # Iterate through the string with the end pointer of the window.
        for end, char in enumerate(s):
            # If the character is already in the map and its last seen index
            # is within the current window, move the start of the window.
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1

            # Update the last seen index of the current character.
            char_map[char] = end

            # Calculate the length of the current window and update max_length.
            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length

# Complexity Analysis:
#
# Time Complexity: O(n)
# We iterate through the string of length `n` only once. The `end` pointer
# moves from left to right, and the `start` pointer also only moves from left
# to right. Each character is visited at most twice (once by `end` and once
# by `start`). Dictionary lookups and insertions are O(1) on average.
#
# Space Complexity: O(min(m, n))
# The space required is for the hash map. In the worst-case scenario, the
# size of the map can be up to the size of the character set `m` (e.g., ASCII)
# or the size of the string `n` if all characters are unique.
