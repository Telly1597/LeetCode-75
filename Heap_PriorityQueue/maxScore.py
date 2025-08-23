import heapq
from heapq import  heappop, heappush
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
       
        pairs = [ (n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs , key=lambda p: p[1], reverse=True)
        n1Sum = 0
        ans = 0
        min_heap = []

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) > k:
                n1Sum -= heappop(min_heap)
            if len(min_heap) == k:
                ans = max(ans, n1Sum * n2)

        return ans