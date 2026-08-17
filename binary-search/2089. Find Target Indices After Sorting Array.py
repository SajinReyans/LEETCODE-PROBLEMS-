class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()

        first=-1
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                right=mid-1
                first=mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if first==-1:
            return []
        left=0
        right=len(nums)-1
        last=-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                last=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return list(range(first,last+1))
                
