class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count_t={}
        count_s={}
        for c in s:
            count_s[c]=count_s.get(c,0)+1
        for c in t:
            count_t[c]=count_t.get(c,0)+1

        count=0
        for key in count_t:
            count+=max(count_t[key]-count_s.get(key,0),0)
        return count
