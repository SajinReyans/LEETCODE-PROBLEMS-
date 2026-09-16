class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        array=s.split(" ")
        result=""
        for i in range(k):
            result+=array[i]
            result+=" "
        return result[0:-1]    
