from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr, rightArr = [0] * len(nums)  , [0] * len(nums)
        left_mult, right_mult = 1, 1

        for i in range(len(nums)):
            j = (len(nums) - 1) - i
            
            leftArr[i] = left_mult
            left_mult *= nums[i]

            rightArr[j] = right_mult
            right_mult *= nums[j]

       
        return [ x * y for x, y in zip(leftArr, rightArr)]