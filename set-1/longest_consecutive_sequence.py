def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if num is the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Expand sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest
