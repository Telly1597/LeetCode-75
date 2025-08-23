from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = [] 

        def backTrack(start, remaining, path):
            if len(path) == k and remaining == 0:
                answer.append(path[:])
                return 

            for i in range(start, 10):
                if remaining - i < 0:
                    break
                path.append(i)
                backTrack(i + 1, remaining - i, path)
                path.pop()

        backTrack(1, n, [])
        return answer