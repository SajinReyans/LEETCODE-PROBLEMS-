class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        seen = set()

        for c in count:
            seen.add(count[c])

        return len(seen) == 1
