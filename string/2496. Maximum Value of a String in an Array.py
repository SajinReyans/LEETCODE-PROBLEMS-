class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        longest=0
        count=0
        for word in strs:
            if word.isdigit():
                count=int(word)
            else:
                count=len(word)
            longest=max(longest,count)
        return longest
