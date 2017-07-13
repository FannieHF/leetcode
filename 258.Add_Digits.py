class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = num
        while (num >= 10):
            sum = 0
            for i in str(num):
                sum += int(i)
            num = sum
        return sum
        

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = num
        while (num >= 10):
            sum = 0
            while (num >= 10):
                sum += num%10
                num /= 10
            sum += num
            num = sum
        return sum
        
