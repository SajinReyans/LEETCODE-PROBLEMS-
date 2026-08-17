class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]>=0:
                right=mid-1
            else:
                left=mid+1
        negative_count=left
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]>0:
                right=mid-1
            else:
                left=mid+1

        positive_count=len(nums)-left
        return max(positive_count,negative_count)
