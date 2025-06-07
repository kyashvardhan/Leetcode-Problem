def subarraySum(nums, k):
    count = 0
    current_sum = 0
    prefix_map = {0: 1}  # to handle subarrays that start from index 0

    for num in nums:
        current_sum += num
        if (current_sum - k) in prefix_map:
            count += prefix_map[current_sum - k]
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count
