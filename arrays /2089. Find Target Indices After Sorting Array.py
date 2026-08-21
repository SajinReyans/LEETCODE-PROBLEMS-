class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        result = []
        for index, element in enumerate(nums):
            if element == target :
                result.append(index)
        return result

