class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping={}
        
        i=97
        
        for k in key:
            if k!=" " and k not in mapping:
                mapping[k]=chr(i)
                i+=1
        result=""
        for m in message:
            if m!=" ":
                result+=mapping[m]
            else:
                result+=" "
        return result
