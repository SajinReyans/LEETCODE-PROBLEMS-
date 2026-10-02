class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result=[]
        
        for word in words:
             
            flag=True
                    
            s_to_t={}
            t_to_s={}


            for s,t in zip(word,pattern):
                if s in s_to_t and s_to_t[s]!=t:
                    flag=False
                    break
                if t in t_to_s and t_to_s[t]!=s:
                    flag=False
                    break
                s_to_t[s]=t
                t_to_s[t]=s
            if flag:
                result.append(word)
        return result
                    
