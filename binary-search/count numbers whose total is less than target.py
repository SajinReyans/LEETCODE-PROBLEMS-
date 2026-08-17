class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        count=0
        nums.sort()
        while(left<=right):
            total=nums[left]+nums[right]
            if total<target:

                count+=(right-left)
                left+=1

            else:
                right-=1
        return count
