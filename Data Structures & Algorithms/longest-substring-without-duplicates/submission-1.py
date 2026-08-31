class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = {}
        start = 0
        longest = 0

        for i, c in enumerate(s):
            if c in chars and chars[c] >= start:
                start = chars[c] + 1

            chars[c] = i
            longest = max(longest, i - start + 1)
        
        return longest
            



        
        