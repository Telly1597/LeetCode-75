import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcdRes = math.gcd(len(str1), len(str2))
        if str1[0:gcdRes] != str2[0:gcdRes]:
            return ""
    
        i, j = 0, 0

        while i < len(str1):
            if str1[i: i + gcdRes] != str1[0:gcdRes]:
                return ""
            i += gcdRes

        while j < len(str2):
            if str2[j: j + gcdRes] != str1[0:gcdRes]:
                return ""
            j += gcdRes
        
        return str1[0:gcdRes]


