class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        current =word
        count=0
        while current in sequence:
            current+=word
            count+=1
        return count
