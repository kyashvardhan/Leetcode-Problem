# LeetCode Problem 1: Two Sum
#
# Problem Statement:
# Given an array of integers `nums` and an integer `target`, return the indices
# of the two numbers such that they add up to `target`.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
#
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]

from typing import List

class Solution:
    """
    Solves the Two Sum problem.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list that sum up to the target.

        This solution uses a hash map (dictionary in Python) to achieve a
        single-pass solution. We iterate through the list, and for each element,
        we calculate the complement needed to reach the target.

        If the complement is already in our hash map, we have found our pair.
        The value stored in the hash map is the index of the complement.

        If the complement is not in the map, we add the current number and its
        index to the map for future lookups.

        Args:
            nums: A list of integers.
            target: The target integer sum.

        Returns:
            A list containing the indices of the two numbers.
        """
        # Create a hash map to store numbers we've seen and their indices.
        # Key: number, Value: index
        num_map = {}

        # Iterate through the list with both index and value.
        for i, num in enumerate(nums):
            # Calculate the complement we need to find.
            complement = target - num

            # Check if the complement exists in our map.
            if complement in num_map:
                # If it exists, we've found the solution.
                # Return the index of the complement and the current index.
                return [num_map[complement], i]

            # If the complement is not in the map, add the current number
            # and its index to the map.
            num_map[num] = i

        # In case no solution is found, though the problem statement guarantees
        # one exists. Returning an empty list is a common practice.
        return []

# Complexity Analysis:
#
# Time Complexity: O(n)
# We iterate through the list of `n` elements only once. Each lookup and
# insertion in the hash map takes, on average, O(1) time.
#
# Space Complexity: O(n)
# In the worst-case scenario, we might have to store all `n` elements in the
# hash map before finding the pair. This happens if the pair is at the very
# end of the list or doesn't exist.
