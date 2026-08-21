class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        nums.sort()
        merged=[]
        for n in nums:
            if not merged or merged[-1][1]<n[0]:
                merged.append(n)
            else:
                merged[-1][1]=max(merged[-1][1],n[1])
        count=0
        for i in range(len(merged)):
            count+=merged[i][1]-merged[i][0]+1
        return count
