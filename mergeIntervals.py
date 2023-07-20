"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

def merge(self, intervals: List[List[int]]) -> List[List[int]]:

    if intervals == [] or len(intervals) == 1:
        return intervals

    # Initialize empty list to store the merged intervals.
    result = []
    intervals.sort()

    for interval in intervals:
        # Check if it overlaps
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        # If it doesn't overlap
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result
