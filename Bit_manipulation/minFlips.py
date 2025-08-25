class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1
         
            if cbit == 1:
                if (abit | bbit) == 0:
                    flips += 1
            else:
                flips += abit + bbit

            a >>= 1
            b >>= 1
            c >>= 1
        return flips