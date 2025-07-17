def canCompleteCircuit(gas, cost):
    total_tank = 0
    current_tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        # If we can't reach station i+1 from i
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    return start_index if total_tank >= 0 else -1
