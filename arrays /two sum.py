class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference not in d:
                d[nums[i]]=i
            else:
                return [d[difference],i]
