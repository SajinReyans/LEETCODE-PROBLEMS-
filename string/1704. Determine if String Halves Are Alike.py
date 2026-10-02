class Solution(object):
    def halvesAreAlike(self, s):
        vowels = "aeiouAEIOU"
        
        first = s[:len(s)//2]
        second = s[len(s)//2:]

        count1 = sum(c in vowels for c in first)
        count2 = sum(c in vowels for c in second)

        return count1 == count2
