from collections import defaultdict

def numSubarraysWithSum(nums, goal):
    count = 0
    prefix_sum = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # base case

    for num in nums:
        prefix_sum += num
        count += prefix_counts[prefix_sum - goal]
        prefix_counts[prefix_sum] += 1

    return count
