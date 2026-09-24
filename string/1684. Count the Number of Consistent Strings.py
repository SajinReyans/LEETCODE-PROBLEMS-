class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for word in words:
            seen=set(word)
            count+=1
            for see in seen:
                
                if see not in allowed:
                    count-=1
                    break
        return count
            
