class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common={}
        for word in words[0]:
            common[word]=common.get(word,0)+1
     
        for word in words[1:]:
            count={}
            for c in word:
                count[c]=count.get(c,0)+1

            for c in common:
                if c in count:
                    common[c]=min(common[c],count[c])
                else:
                    common[c]=0
        result=[]
        for c in common:
            for _ in range(common[c]):
                result.append(c)
        return result
