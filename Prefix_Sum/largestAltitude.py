from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heighest, n = 0, len(gain) 
        prev, cur = 0, 0
   
        for i in range(n):
            cur = prev + gain[i]
            prev = cur 
            heighest = max(heighest, cur)
       
        return heighest