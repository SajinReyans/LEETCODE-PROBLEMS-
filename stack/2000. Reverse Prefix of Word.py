class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        str2=""
        if ch not in word:
            return word
        for i ,n in enumerate(word):
            if ch==n:
                str2=word[:i+1]
                str2=str2[::-1]
                str2=str2+word[i+1:]
                break
        return str2
