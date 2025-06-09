def subarraySum(nums, k):
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # sum: frequency

    for num in nums:
        current_sum += num
        diff = current_sum - k
        count += prefix_sums.get(diff, 0)
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count
