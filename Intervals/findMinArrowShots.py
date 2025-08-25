from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        arrow = 1
        last = points[0][1]
        
        for start , end in points[1:]:
            if start > last:
                arrow += 1
                last = end 

        return arrow 