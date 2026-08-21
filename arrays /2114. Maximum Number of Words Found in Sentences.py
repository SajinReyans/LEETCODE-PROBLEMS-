class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result=[]
        for sentence in sentences:
            result.append(len(sentence.split()))
        return max(result)
