from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = maxLength =  countZeros = 0
        MAX_ZEROS = 1

        for end in range(len(nums)):
            if nums[end] == 0:
                countZeros += 1

            while countZeros > MAX_ZEROS:
                if nums[start] == 0:
                    countZeros -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)

        # return maxLength - 1. since we are deleting an element. 
        return maxLength - 1