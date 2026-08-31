class Solution:
    def minWindow(self, s: str, t: str) -> str:

        charF = {}

        for c in t:
            charF[c] = 1 + charF.get(c, 0)


        seen = {}
        charsSat = 0
        charsNeed = len(set(t))
        start = 0
        best = [-1, -1]

        for end in range(len(s)):
            c = s[end]
            
            seen[c] = 1 + seen.get(c, 0)
            
            if c in charF and seen[c] == charF[c]:
                charsSat += 1

            while charsSat == charsNeed:
                if best == [-1, -1] or best[1] - best[0] > end - start:
                    best = [start, end]
                
                seen[s[start]] -= 1
                if s[start] in charF and seen[s[start]] < charF[s[start]]:
                    charsSat -= 1

                start += 1
        
        l, r = best
        return s[l:r+1] if best != [-1, -1] else ""

            


        