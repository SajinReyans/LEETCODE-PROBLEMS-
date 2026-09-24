class Solution(object):
    def vowelStrings(self, words, left, right):
        count = 0
        vowels = "aeiou"

        for i in range(left, right + 1):
            word = words[i]

            if word[0] in vowels and word[-1] in vowels:
                count += 1

        return count
