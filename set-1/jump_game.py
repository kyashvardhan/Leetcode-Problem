def canJump(nums):
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  # Can't reach this point
        max_reach = max(max_reach, i + jump)

    return True
