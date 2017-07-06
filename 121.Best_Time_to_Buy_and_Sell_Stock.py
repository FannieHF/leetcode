class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        
        mini = prices[0]
        diff = 0
        for num in prices[1:]:
            if num-mini > diff:
                diff = num-mini
            if num < mini:
                mini = num
        return diff
