class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word="".join(word1)
        words="".join(word2)
        if word==words:
            return True
        return False
        
