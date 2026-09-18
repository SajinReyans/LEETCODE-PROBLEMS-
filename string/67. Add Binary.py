class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        a=a[::-1]
        b=b[::-1]
        result=[]
        for i in range(max(len(a),len(b))):
            digit_a=(a[i] if i<len(a) else 0)


            digit_b=(b[i] if i<len(b) else 0)
            total=int(digit_a)+int(digit_b)+carry
            result.append(str(total%2))
            carry=total//2
        if carry:
            result.append("1")
        return "".join(result[::-1])

