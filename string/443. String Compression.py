class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read=0
        write=0
        result=[]
        while read<len(chars):
            count=0
            current=chars[read]
            while read<len(chars) and current==chars[read]:
                count+=1
                read+=1
            chars[write]=current
            write+=1
            if count>1:
                for number in str(count):
                    chars[write]=number
                    write+=1
        return write          
