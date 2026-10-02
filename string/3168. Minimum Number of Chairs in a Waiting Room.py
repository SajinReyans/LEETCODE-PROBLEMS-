class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        count=0
        for ch in s:
            if ch=="E":
                count+=1
            else:
                count-=1
            result=max(result,count)
        return result
