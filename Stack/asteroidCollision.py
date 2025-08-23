from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) < 2:
            return asteroids

        stack = []
        for a in asteroids:
            stack.append(a)
            # only collide when prev is right-moving and current is left-moving
            while len(stack) >= 2 and stack[-2] > 0 and stack[-1] < 0:
                right = stack[-2]
                left = stack[-1]
                if abs(right) == abs(left):
                    stack.pop()      # remove left
                    stack.pop()      # remove right
                elif abs(right) < abs(left):
                    stack.pop(-2)    # remove the right one at index -2
                else:
                    stack.pop()      # remove left
                    break
        return stack