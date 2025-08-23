from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            else:
                return 0 >= n

        numFlowersPlanted = 0
        for i in range(len(flowerbed)):

            # values that are in the middle
            if i != 0 and i != len(flowerbed) - 1:
                if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                    if flowerbed[i] == 0:
                        numFlowersPlanted += 1
                        flowerbed[i] = 1
            # we encounter 0 and index 0
            elif i == 0:
                if flowerbed[i + 1] != 1:
                    if flowerbed[i] == 0:
                        numFlowersPlanted += 1
                        flowerbed[i] = 1
            # we encounter 0 and index i - 1
            else:
                if flowerbed[i- 1] != 1:
                    if flowerbed[i] == 0:
                        numFlowersPlanted += 1
                        flowerbed[i] = 1


        return numFlowersPlanted >= n