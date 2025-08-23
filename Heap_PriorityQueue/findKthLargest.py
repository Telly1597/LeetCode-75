import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for val in nums:
            if len(heap) < k:
                heapq.heappush(heap, val)
            elif val > heap[0] :
                heapq.heappop(heap)
                heapq.heappush(heap, val)
            
        return heap[0]
        # return heapq.nlargest(k, nums)[-1]