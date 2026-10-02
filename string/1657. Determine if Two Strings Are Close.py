class Solution(object):
    def closeStrings(self, word1, word2):
        if set(word1) != set(word2):
            return False

        count1 = {}
        count2 = {}

        for c in word1:
            count1[c] = count1.get(c, 0) + 1

        for c in word2:
            count2[c] = count2.get(c, 0) + 1

        return sorted(count1.values()) == sorted(count2.values())
