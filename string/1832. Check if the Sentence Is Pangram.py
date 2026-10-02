import string
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        constant=string.ascii_lowercase
        for c in constant:
            if c not in sentence:
                return False
        return True
        
