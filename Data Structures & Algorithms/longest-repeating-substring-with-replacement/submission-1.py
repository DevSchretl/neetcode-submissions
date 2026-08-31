class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charSet = set(s)
        largest = 0

        for c in charSet:
            count = 0
            start = 0

            for end in range(len(s)):

                if c == s[end]:
                    count += 1

                while end - start + 1 - k > count:
                    if s[start] == c:
                        count -= 1
                    start += 1

                largest = max(end - start + 1, largest)
                
        return largest

            




        