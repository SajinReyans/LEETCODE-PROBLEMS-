class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count={}
        for char in s:
            count[char]=count.get(char,0)+1
        result=""
        for c ,freq in sorted(count.items() ,key=lambda x:x[1], reverse=True):

            result+=c*freq
        return result
