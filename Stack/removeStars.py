class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            while len(stack) > 0 and stack[-1] == '*':
                stack.pop()
                stack.pop()
            stack.append(s[i])
            
        if len(stack) > 0 and stack[-1] == '*':
            stack.pop()
            stack.pop()
          
        return ''.join(stack)