class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        r=['']*len(s)
        for char,index in zip(s,indices):
            r[index]=char
        return "".join(r)        
