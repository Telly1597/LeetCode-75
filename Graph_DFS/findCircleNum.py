from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for v in range(n):
                if not visited[v] and isConnected[u][v] == 1:
                    dfs(v)

        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
                
        return provinces