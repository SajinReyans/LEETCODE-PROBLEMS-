class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0#window size
        longest=-1
        count=0
        while(k<len(nums)):
            if nums[k]==1:
                count+=1
                k+=1
            else:
                longest=max(longest,count)
                count=0
                k+=1
        longest=max(longest,count)
        return longest
