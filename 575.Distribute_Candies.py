class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        type = set()
        for i in candies:
            type.add(i)
            
        return min(len(type),len(candies)/2)
