class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        back = 0
        longest = 0
        seen = set()

        for i in range(len(s)):

            if s[i] in seen:
                while s[back] != s[i]:
                    seen.remove(s[back])
                    back += 1
                back += 1
            else:
                seen.add(s[i])
            
            longest = max(longest, i - back + 1)
        
        return longest;


# find the longest substring where all characters are different
# "a" -> 1, "aaa" -> 1, "caba" -> 3, "" -> 0
            



        
        