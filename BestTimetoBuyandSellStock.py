class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        glo_profit = 0
        lowest_price = prices[0]
        #for i in range(1,2):
            #print(i)
        for i in range(1, len(prices)):
            lowest_price = min(lowest_price,prices[i])
            glo_profit = max(glo_profit, prices[i]-lowest_price)
                
        return glo_profit

s = Solution()
print(s.maxProfit([1,2]))