class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result=[]
        for i in range(len(words)):
            
            seen1=set(words[i])
            for j in range(i+1,len(words)):
                seen2=set(words[j])
                
                if seen1==seen2:
                    result.append((i,j))
        return len(result)

                
