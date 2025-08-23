from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        slow = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] , nums[slow] = nums[slow], nums[i]
                slow += 1