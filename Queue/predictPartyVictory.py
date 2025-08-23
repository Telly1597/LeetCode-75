from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str: 
        rad, dirr = deque(), deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                rad.append(i)
            else:
                dirr.append(i)
        next_index = len(senate)
        while rad and dirr:
            if rad[0] < dirr[0]:
                rad.append(next_index)
            else:
                dirr.append(next_index)
            dirr.popleft()
            rad.popleft()
            next_index += 1

        return "Radiant" if rad else "Dire"