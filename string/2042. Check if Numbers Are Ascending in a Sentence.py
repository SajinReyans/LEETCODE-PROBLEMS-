class Solution(object):
    def areNumbersAscending(self, s):
        words = s.split()
        number = []

        for c in words:
            if c.isdigit():
                number.append(int(c))

        for i in range(1, len(number)):
            if number[i] <= number[i - 1]:
                return False

        return True
