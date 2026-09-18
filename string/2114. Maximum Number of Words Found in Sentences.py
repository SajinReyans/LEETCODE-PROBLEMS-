class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result=[]
        for i in sentences:
            result.append(len(i.split()))

        return max(result)        
