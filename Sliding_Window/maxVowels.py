class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vSet = set(['a','e', 'i','o','u'])
        cur_sum = maxVal  = slow  = 0
        for i in range(len(s)):
            if s[i] in vSet:
                cur_sum += 1

            if i >= k - 1:
                maxVal = max(maxVal, cur_sum)
                cur_sum = cur_sum - 1 if s[slow] in vSet else cur_sum
                slow += 1

        return maxVal
   