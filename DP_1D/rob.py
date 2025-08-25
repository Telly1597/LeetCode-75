from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        house_1, house_2 = 0, 0 
        for num in nums:
            house_1, house_2 = max(house_1, house_2 + num), house_1
        
        return house_1