class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join([char for char in s.lower() if char.isalnum()])

        start = 0
        end = len(clean) - 1

        while start < end:  
            if clean[start] != clean[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
        