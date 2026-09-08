class Solution(object):

    def isSubsequence(self, s, t):

        """

        :type s: str

        :type t: str

        :rtype: bool

        """

        

        one=0

        two=0

        while(one<len(s) and two<len(t)):

            if(s[one]==t[two]):

                one+=1

                

            two+=1

        return one==len(s)

