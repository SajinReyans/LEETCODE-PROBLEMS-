class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        required={}
        for word in words2:
            count={}
            for c in word:
                count[c]=count.get(c,0)+1
            for c in count:
                required[c]=max(required.get(c,0),count[c])
        result=[]
        for word in words1:
            count={}
            for c in word:
                count[c]=count.get(c,0)+1
            flag=True

            for c in required:
                if count.get(c,0)<required[c]:
                    flag=False
                    break
            if flag:
                result.append(word)
        return result
