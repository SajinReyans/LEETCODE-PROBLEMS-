class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets=set(nums)
        longest=0
        for num in sets:
            if num-1 not in sets:
                next_num=num+1
                length=1
                while next_num in sets:
                    next_num+=1
                    length+=1
                longest=max(longest,length)
        return longest
