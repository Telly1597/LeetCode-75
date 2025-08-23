from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_map1, hash_map2 = {}, {}

        for i in range(len(nums1)):
            if nums1[i] not in hash_map1:
                hash_map1[nums1[i]] = True

        for i in range(len(nums2)):
            if nums2[i] not in hash_map2:
                hash_map2[nums2[i]] = True
                
        ans0 = set()
        ans1 = set()

        for i in range(len(nums1)):
            if nums1[i] not in hash_map2:
                ans0.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in hash_map1:
                ans1.add(nums2[i])
     
        return [ list(ans0), list(ans1)]