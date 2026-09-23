class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result=0
        count={}
        for c in chars:
            if c in count:
                count[c]+=1

            else:
                count[c]=1
        for word in words:
            temp={}
            for c in word:
                if c not in temp:
                    temp[c]=1
                else:
                    temp[c]+=1
            possible=True
            for c in temp:
                if   c not in count or temp[c]>count[c]:
                    possible=False
                    break
            if possible:
                result+=len(word)
        return result
