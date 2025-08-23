from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:


        def isEquals(ar1: List[int], ar2:List[int]) -> int:
            # guarantee to be the same length. since we are dealing with n X n matrix.
            for i in range(len(ar1)):
                if ar1[i] != ar2[i]:
                    return False
            return True 

        n = len(grid)
        cols = list(zip(*grid))
        
        countNumEquals = 0
        for i in range(n):
            for j in range(n):
                if isEquals(grid[i], list(cols[j])):
                    countNumEquals += 1

        return countNumEquals