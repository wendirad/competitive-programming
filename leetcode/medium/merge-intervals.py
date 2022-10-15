class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals) - 1
        start = 0
        while start < n:
            if intervals[start + 1][0] <= intervals[start][1]:
                intervals[start][1] = max(intervals[start + 1][1], intervals[start][1])
                intervals.pop(start+1)
                n -= 1
            else:
                start += 1
        return intervals
            