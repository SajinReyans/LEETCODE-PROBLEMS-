class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left=0
        right=n-1
        pos=n-1
        result=[0]*n
        while(left<=right):
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]*nums[left]
                left+=1
            else:
                result[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return result  
