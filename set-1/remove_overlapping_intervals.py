def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    non_overlap_count = 1
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:
            non_overlap_count += 1
            prev_end = end

    return len(intervals) - non_overlap_count
