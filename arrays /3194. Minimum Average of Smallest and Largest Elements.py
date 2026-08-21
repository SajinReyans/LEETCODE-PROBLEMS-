class Solution:

    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()

        left=0

        right=len(nums)-1

        average=[]

        while left<right:

            average.append((nums[left]+nums[right])/2)

            left+=1

            right-=1

        return min(average)    
