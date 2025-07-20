class Solution:
    """
    This class provides a solution to the LeetCode problem 217: Contains Duplicate.
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array `nums`, this function returns `true` if any value 
        appears at least twice in the array, and it returns `false` if every 
        element is distinct.

        Args:
            nums: A list of integers.

        Returns:
            True if the list contains duplicates, False otherwise.
        
        Example 1:
        Input: nums = [1,2,3,1]
        Output: true

        Example 2:
        Input: nums = [1,2,3,4]
        Output: false

        Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
        """
        
        # We can use a hash set to store the numbers we have seen so far.
        # A set is a collection of unique elements, so if we try to add an
        # element that is already in the set, we know that we have a duplicate.
        
        seen = set()
        
        # Iterate over the numbers in the list.
        for num in nums:
            # If the number is already in the set, we have a duplicate.
            if num in seen:
                return True
            # Otherwise, add the number to the set.
            seen.add(num)
            
        # If we get to the end of the list without finding any duplicates,
        # then all the elements are distinct.
        return False

# You can test the solution with a few examples.
if __name__ == '__main__':
    solver = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {solver.containsDuplicate(nums1)}") # Expected: True
    
    print("-" * 20)
    
    # Example 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: {nums2}")
    print(f"Output: {solver.containsDuplicate(nums2)}") # Expected: False

    print("-" * 20)

    # Example 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: {nums3}")
    print(f"Output: {solver.containsDuplicate(nums3)}") # Expected: True
