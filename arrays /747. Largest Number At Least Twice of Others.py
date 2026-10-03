class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        large=-1
        index=-1
        for i,num in enumerate(nums):
            if num>large:
                large=num
                index=i
        for i in range(len(nums)):
            if large<nums[i]*2 and i!=index:
                return -1
        return index
