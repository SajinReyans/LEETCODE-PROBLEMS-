class Solution(object):
    def makeFancyString(self, s):
        result = ""

        for c in s:
            if len(result) < 2 or not (result[-1] == c and result[-2] == c):
                result += c

        return result
