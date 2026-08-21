class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lowest=float('inf')
        closest=float('inf')
        for num in nums:
            new =abs(num)
            if ((lowest>new)or(closest<num and lowest==new)):
                lowest=new
                closest=num
        return closest
