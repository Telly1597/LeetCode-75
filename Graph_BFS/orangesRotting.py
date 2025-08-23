from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh_oranges == 0:
            return 0

        minute = 0
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                x , y = queue.popleft()
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if 0 <= new_x < rows  and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_oranges -= 1
                        queue.append((new_x, new_y))
            minute += 1

                    
        return minute if fresh_oranges == 0 else - 1