class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0

        for p in prices:
            if buy > p:
                buy = p
            
            if p - buy > maxp:
                maxp = p - buy
        
        return maxp
            




        

        