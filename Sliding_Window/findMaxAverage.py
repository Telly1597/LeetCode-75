from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])

        for fast in range(k, len(nums)):
            cur_sum += nums[fast] - nums[fast - k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k