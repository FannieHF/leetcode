class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pointer= 0
        zero_num = 0
        while pointer < (length-zero_num):
            if nums[pointer] == 0:
                nums[pointer:] = nums[pointer+1:]+[0]
                pointer -= 1
                zero_num += 1
            pointer += 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if (nums is None or len(nums) == 0):
            return
        
        pointer = 0
        for i in nums:
            if i is not 0:
                nums[pointer] = i
                pointer += 1
        
        while pointer < len(nums):
            nums[pointer] = 0
            pointer += 1
            
            
