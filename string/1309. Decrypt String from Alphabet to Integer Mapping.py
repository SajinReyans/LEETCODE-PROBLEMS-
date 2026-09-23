class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """

        mapping={}
        for i in range(1,27):
            if i<=9:
                mapping[str(i)]=chr(96+i)
            else:
                mapping[str(i)+"#"]=chr(96+i)
        result=[]
        i=len(s)-1
        while i >= 0:
            if s[i] == "#":
                string = s[i-2:i+1]
                result.append(mapping[string])
                i -= 3
            else:
                result.append(mapping[s[i]])
                i -= 1

        return "".join(result[::-1])

            
