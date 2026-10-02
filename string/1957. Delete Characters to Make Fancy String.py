class Solution:
    def makeFancyString(self, s):
        result = []
        previous_char = ""
        consecutive_count = 0

        for char in s:
            if char != previous_char:
                previous_char = char
                consecutive_count = 0

            if consecutive_count < 2:
                result.append(char)
                consecutive_count += 1

        return "".join(result)
