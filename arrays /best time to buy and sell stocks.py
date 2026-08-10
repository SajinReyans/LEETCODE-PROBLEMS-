class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        negative=float('inf')
        positive=-1
        for i in range(len(prices)):
            price=prices[i]
            if negative>price:
                negative=price
            profit=price-negative
            if profit>positive:
                positive=profit

        return positive
