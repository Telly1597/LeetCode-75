from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rows, cols = len(maze), len(maze[0])
        start, end = entrance

        queue = deque([(start, end, 0)])
        maze[start][end] = '+'

        while queue:
            x, y, steps = queue.popleft()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != '+':

                    # found boundary
                    if new_x in [0, rows - 1] or new_y in [0, cols - 1]:
                        return steps + 1
                    maze[new_x][new_y] = '+'
                    queue.append((new_x, new_y, steps + 1))
        return -1