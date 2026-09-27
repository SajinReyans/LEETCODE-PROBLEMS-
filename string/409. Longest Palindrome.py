class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count={}
        length=0
        odd=False
        for c in s:
            count[c]=count.get(c,0)+1
        for value in count.values():
            if value%2==0:
                length+=value
            else:
                length+=value-1
                odd=True
        if odd:
            length+=1
        return length
