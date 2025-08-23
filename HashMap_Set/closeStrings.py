from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        m1 , m2,  = Counter(word1) , Counter(word2)
        
        s1 = list()

        for i in m1:
            if i not in m2:
                return False
            s1.append(m1[i])

        for i in m2:
            if m2[i] not in s1:
                return False
            else:
                s1.remove(m2[i])

        return True
        