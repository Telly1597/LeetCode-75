from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for num in spells:
            left, right = 0, len(potions) - 1
            midFound = False

            while left <= right:
                mid = left + (right - left ) // 2
                if potions[mid] * num >= success:
                    right = mid - 1 
                else:
                    left  = mid + 1
            
            ans.append(len(potions) - left)

        return ans