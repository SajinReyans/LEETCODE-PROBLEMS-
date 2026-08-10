class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        for key,value in d.items():
            if n//2<value:
                return key
