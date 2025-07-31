# Problem Statement:
# Given two sorted arrays `nums1` and `nums2` of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from typing import List

class Solution:
    """
    Solves the Median of Two Sorted Arrays problem.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays.

        This solution uses a binary search approach to achieve the required
        O(log(min(m, n))) time complexity. The core idea is to partition
        the two arrays into two halves, a "left part" and a "right part",
        such that every element in the left part is less than or equal to
        every element in the right part, and the number of elements in both
        parts is equal (or the left part has one more element if the total
        number of elements is odd).

        We perform the binary search on the smaller of the two arrays to
        optimize performance.

        Let the smaller array be A and the larger be B.
        We partition A at index `i` and B at index `j`.
        `partitionX` is the number of elements in the left part of A.
        `partitionY` is the number of elements in the left part of B.

        We need to satisfy:
        1. `partitionX` + `partitionY` = (m + n + 1) / 2
        2. `max(left part of A)` <= `min(right part of B)`
        3. `max(left part of B)` <= `min(right part of A)`

        If these conditions are met, we have found the correct partition.
        The median is then calculated based on whether the total number of
        elements is even or odd.

        Args:
            nums1: The first sorted array.
            nums2: The second sorted array.

        Returns:
            The median of the two combined sorted arrays.
        """
        # Ensure nums1 is the smaller array to optimize the binary search.
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        x, y = len(nums1), len(nums2)
        low = 0
        high = x

        while low <= high:
            # Partition the smaller array (nums1).
            partitionX = (low + high) // 2
            # Calculate the partition for the larger array (nums2) based on partitionX.
            # The +1 handles both even and odd total lengths correctly.
            partitionY = (x + y + 1) // 2 - partitionX

            # Get the boundary elements for the partitions.
            # maxLeftX is the max element on the left side of partition in nums1.
            # minRightX is the min element on the right side of partition in nums1.
            maxLeftX = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX != x else float('inf')

            # Do the same for nums2.
            maxLeftY = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY != y else float('inf')

            # Check if we have found the correct partition.
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # The partition is correct, now calculate the median.
                # If the total length is even.
                if (x + y) % 2 == 0:
                    median = (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                    return median
                else:
                    # If the total length is odd.
                    median = float(max(maxLeftX, maxLeftY))
                    return median
            elif maxLeftX > minRightY:
                # We are too far on the right side for partitionX.
                # Go to the left in nums1.
                high = partitionX - 1
            else:
                # We are too far on the left side for partitionX.
                # Go to the right in nums1.
                low = partitionX + 1
        
        # Should not happen if inputs are sorted arrays.
        raise ValueError("Input arrays are not sorted.")


# Complexity Analysis:
#
# Time Complexity: O(log(min(m, n)))
# The binary search is performed on the smaller of the two arrays. If `m` is the
# length of the smaller array, the search space is halved in each step, leading
# to a logarithmic time complexity.
#
# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space to store a few variables
# for the indices and boundary values, regardless of the input size.
