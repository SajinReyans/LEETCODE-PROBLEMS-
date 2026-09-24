class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        
        seen=set()
        end=-1
        for i,c in enumerate(s):
            if c not in seen:
                start=i

                for j in range(i+1,len(s)):
                    if s[j]==c:
                        end=j
                diff=end-start-1
                if distance[ord(c)-ord('a')]!=diff:
                    return False
                seen.add(c)
        return True
                    
