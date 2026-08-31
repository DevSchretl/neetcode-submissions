from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                    
                close = stack.pop()
                if close == '(' and c != ')':
                    return False
                if close == '[' and c != ']':
                    return False
                if close == '{' and c != '}':
                    return False
        
        return len(stack) == 0
                