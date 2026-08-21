class Solution(object):

    def isArraySpecial(self, nums):

        """

        :type nums: List[int]

        :rtype: bool

        """

        def parity(x):

            if x%2==0:

                return 'even'

            else: 

                return 'odd'

        for i in range(1,len(nums)):

            if parity(nums[i])==parity(nums[i-1]):

                return False            


        return True  
