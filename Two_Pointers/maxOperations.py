from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0 , len(nums) -1
        countNumPairs = 0
        while start < end:
            if nums[start] + nums[end] == k:
                countNumPairs += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            else:
                end -= 1

        return countNumPairs
        