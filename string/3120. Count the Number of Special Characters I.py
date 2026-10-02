class Solution(object):
    def numberOfSpecialChars(self, word):
        result = 0

        for c in string.ascii_lowercase:
            if c in word and c.upper() in word:
                result += 1

        return result
