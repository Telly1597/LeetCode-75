from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        num_deleted =  0
        last_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < last_interval[1]:
                num_deleted += 1
                if interval[1] < last_interval[1]:
                    last_interval = interval
            else:
                last_interval = interval
        return num_deleted 