from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    window = Counter(s2[:len(s1)])

    if window == s1_count:
        return True

    for i in range(len(s1), len(s2)):
        start_char = s2[i - len(s1)]
        end_char = s2[i]

        window[end_char] += 1
        window[start_char] -= 1

        if window[start_char] == 0:
            del window[start_char]

        if window == s1_count:
            return True

    return False
