class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1


        heap = [(0, 0)] * k
        heapq.heapify(heap)

        for i in freqs.keys():

            if freqs[i] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freqs[i], i))
        
        res = []

        for t in heap:
            res.append(t[1])

        return res
        