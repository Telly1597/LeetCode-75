from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxVal = 0

        while start < end:
            maxVal = max(maxVal, min(height[start], height[end] ) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxVal