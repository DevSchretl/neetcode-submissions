class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        list.sort(intervals)

        merged = []
        start = 0
        m = 0

        for i in range(len(intervals)-1):
            m = max(m, intervals[i][1])
            if m < intervals[i+1][0]:
                merged.append([intervals[start][0], m])
                start = i+1
        
        merged.append([intervals[start][0], max(m, intervals[len(intervals)-1][1])])

        return merged
        