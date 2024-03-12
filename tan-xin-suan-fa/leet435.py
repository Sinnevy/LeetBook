def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    n = len(intervals)
    sorted_matrix = sorted(intervals, key=lambda x: x[1])
    removed = 0
    prev = sorted_matrix[0][1]
    for i in range(1, n, 1):
        if(intervals[i][0] < prev):
            removed += 1
        else:
            prev = intervals[i][1]
    return removed


if __name__ == '__main__':
    print(eraseOverlapIntervals([[1, 2], [2, 4], [1, 3]]))
