class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        start=0
        end=start+10
        result=[]
        while start<end and end<=len(s):
            result.append(s[start:end])
            end+=1
            start+=1
        count={}
        final=[]
        for c in result:
            count[c]=count.get(c,0)+1
        for key,value in count.items():
            if value>1:
                final.append(key)
        return final
                
        
