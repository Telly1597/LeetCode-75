from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hash_table = {
            "2" : ["a", "b", "c"], 
            "3" : ["d", "e", "f"], 
            "4" : ["g", "h", "i"], 
            "5" : ["j", "k", "l"], 
            "6" : ["m", "n", "o"], 
            "7" : ["p", "q", "r", "s"], 
            "8" : ["t", "u", "v"], 
            "9" : ["w", "x", "y", "z"]
        }

        def backTrack(i: int, currStr: str):
            if len(currStr) == len(digits):
                res.append(currStr)
                return 
            for c in hash_table[digits[i]]:
                backTrack(i + 1, currStr + c)
                
        if digits:
            backTrack(0, "")

        return res