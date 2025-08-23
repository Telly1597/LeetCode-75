class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == len(t):
            if s == t:
                return True
            else:
                return False
        s_index = 0

        for i in range(len(t)):
            if s_index < len(s) and t[i] == s[s_index]:
                s_index += 1
            elif s_index == len(s):
                return True
        
        return s_index == len(s)