class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        jewel_set=set(jewels)
        for stone in stones:
            if stone in jewel_set:
                count+=1
            
        return count
            
