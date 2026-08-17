class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left=1
        right=num
        while(left<=right):
            mid=(left+right)//2
            result=mid*mid
            if result==num:
                return True
            elif result<num:
                left=mid+1
            else:
                right=mid-1
        return False
