from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        arr = []
        for candy in candies:
            maxCandies = max(maxCandies, candy)

        for candy in candies:
            if candy + extraCandies >= maxCandies:
                arr.append(True)
            else:
                arr.append(False)

        return arr
    
