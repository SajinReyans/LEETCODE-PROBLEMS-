class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minVal=min(list([len(string) for string in strs])) 
        compare = strs[0]
        for i in range(minVal):
            for string in strs:
                if compare[i]!=string[i]:
                    return strs[0][:i]
        return strs[0][:minVal]
