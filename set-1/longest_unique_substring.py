def lengthOfLongestSubstring(s):
    char_index = {}  # stores characters and their latest index
    left = 0  # start of current window
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  # slide window right

        char_index[s[right]] = right  # update last seen index
        max_len = max(max_len, right - left + 1)

    return max_len
