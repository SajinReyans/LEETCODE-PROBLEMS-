class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first={}
        answer=-1
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]]=i
            else:
                answer=max(answer,i-first[s[i]]-1)
        return answer
