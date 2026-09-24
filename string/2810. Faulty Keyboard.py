class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        for c in s:
            if c=="i":
                result=result[::-1]
            else:
                result+=c
        return result
            
