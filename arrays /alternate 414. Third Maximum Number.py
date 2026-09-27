class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 1:
            return nums[0]
        for i in range(2):
            a = max(nums)
            nums.remove(a)
        if nums:
            return max(nums)    
        return -1
