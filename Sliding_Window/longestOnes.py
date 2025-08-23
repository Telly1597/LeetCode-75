from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return k

        start = numZeros = maxConsecutive1s =  0
        for end in range(len(nums)):
            if nums[end] == 0:
                numZeros += 1
            
            while numZeros > k:
                if nums[start] == 0:
                    numZeros -= 1
                start += 1
            maxConsecutive1s = max(maxConsecutive1s, end - start + 1)
       
      
        return maxConsecutive1s