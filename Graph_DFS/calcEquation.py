from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return - 1.0
            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start].items():
                 if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return res * weight
            return - 1.0


        result = []

        for (C, D) in queries:
            result.append(dfs(C, D, set()))

        return result 