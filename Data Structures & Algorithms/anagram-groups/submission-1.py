class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:

            chars = [0] * 26

            for c in s:
                chars[ord(c) - 97] += 1
            
            groups[tuple(chars)].append(s)
        
        return list(groups.values())

        