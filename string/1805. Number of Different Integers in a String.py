class Solution(object):
    def numDifferentIntegers(self, word):
        
        i = 0

        result=set()
        while(i<len(word)):
            
            if word[i].isdigit():
                
                num=""
                
                while i<len(word) and word[i].isdigit():
                    
                    num+=word[i]
                    i+=1
                result.add(int(num))
            else:
                i+=1
        return len(result)
