class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            if tuple(sorted(s)) in anagrams:
                anagrams[tuple(sorted(s))].append(s)
            else:
                anagrams[tuple(sorted(s))] = [s]
        return list(anagrams.values())

        