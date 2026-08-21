class Solution(object):

    def minimumAverage(self, nums):

        """

        :type nums: List[int]

        :rtype: float

        """

        averages=[]

        nums.sort()

        while nums:

            averages.append((nums[0]+nums[-1])/2.0)

            nums.pop()

            nums.pop(0)

        return min(averages)
