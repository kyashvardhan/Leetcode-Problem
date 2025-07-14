def dailyTemperatures(temperatures):
    stack = []  # stores (index, temp)
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            prev_i, prev_temp = stack.pop()
            result[prev_i] = i - prev_i
        stack.append((i, temp))

    return result
