class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count={}
        for word in words:
            count[word]=count.get(word,0)+1
        result=[]
        for c , freq in sorted(count.items(),key=lambda x:(-x[1],x[0])):
            if k==0:
                break
            else:
                result.append(c)
                k-=1
        return result
