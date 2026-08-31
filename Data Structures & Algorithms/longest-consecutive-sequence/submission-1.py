class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        current = 0

        for n in numset:
            if n-1 not in numset:
                nxt = n
                while nxt in numset:
                    current += 1
                    nxt += 1
                
                if current > longest:
                    longest = current
                current = 0
        
        return longest
        