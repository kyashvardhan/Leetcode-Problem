from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    window_count = {}
    required = len(t_count)
    formed = 0

    l = r = 0
    min_len = float("inf")
    min_window = (0, 0)

    while r < len(s):
        char = s[r]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = (l, r)

            # Shrink the window
            window_count[s[l]] -= 1
            if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                formed -= 1
            l += 1

        r += 1

    if min_len == float("inf"):
        return ""
    return s[min_window[0]:min_window[1] + 1]
