class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = s.lower().replace(" ", "")

        start = 0
        end = len(clean) - 1

        while start < end:
            while start < end and clean[start].isalnum() == False:
                start += 1
            while start < end and clean[end].isalnum() == False:
                end -= 1
            
            if clean[start] != clean[end]:
                return False
            
            start += 1
            end -= 1
        
        return True
        