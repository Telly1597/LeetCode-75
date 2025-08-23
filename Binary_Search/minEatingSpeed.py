import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            cur_h = 0
            for num in piles:
                cur_h += math.ceil(num / mid)
                
            if cur_h <= h:
                right = mid 
            else:
                left = mid + 1
        
        return left