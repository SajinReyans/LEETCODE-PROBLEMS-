class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=list(num1)[::-1]
        num2=list(num2)[::-1]
        carry=0
        result=[]
        for i in range(max(len(num1),len(num2))):
            digit1=(num1[i] if i<len(num1) else 0)
            digit2=(num2[i] if i<len(num2) else 0)
            total=int(digit1)+int(digit2)+carry
            carry=total//10
            result.append(str(total%10))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])
