class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        s1 = list(s)   # ✅ convert to char list

        left = 0
        right = len(s1) - 1

        while left < right:

            while left < right and s1[left] not in vowels:
                left += 1

            while left < right and s1[right] not in vowels:
                right -= 1

            s1[left], s1[right] = s1[right], s1[left]

            left += 1
            right -= 1

        return "".join(s1)
