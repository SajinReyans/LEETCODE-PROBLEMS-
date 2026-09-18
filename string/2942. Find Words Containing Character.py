class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result=[]
        for i, word in enumerate(words):
            for j in word:
                if x==j:
                    result.append(i)
                    break
        return result
