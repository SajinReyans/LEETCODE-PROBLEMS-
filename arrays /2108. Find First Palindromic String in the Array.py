class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def isPalindrome(word):
            return word==word[::-1]
        for i, word in enumerate(words):
            if isPalindrome(word):
                return word
        return ""
