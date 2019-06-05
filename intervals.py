# get sum intervals
def sumIntervals(intervals):
    overlapIntervals = []
    for interval in intervals:
        overlapIntervals += range(interval[0], interval[1])
    return len(set(overlapIntervals))

print(sumIntervals([
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
]))  # // => 9






