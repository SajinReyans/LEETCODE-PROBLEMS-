class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """

        smallest=-1
        index=-1
        for i in range(len(capacity)):

            if itemSize<=capacity[i]:
                if smallest==-1:
                    smallest=capacity[i]
                    index=i
                else:
                    if smallest>capacity[i]:
                        index=i
                        smallest=capacity[i]
        return index
