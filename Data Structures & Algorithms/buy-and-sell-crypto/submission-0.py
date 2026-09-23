class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Diff = 0
        Max_diff = 0
        for i in range (len(prices)-1):
            for j in range(i+1,len(prices)):
                Diff=prices[j]-prices[i]
                Max_diff=max(Diff,Max_diff)
        return Max_diff
                
        
        