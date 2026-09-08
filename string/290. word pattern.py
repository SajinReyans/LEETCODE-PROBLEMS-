class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool

        """

        s_to_t = {}
        t_to_s = {}
        s=s.split()

        if len(s)!=len(pattern):
            return False
        for a, b in zip(pattern, s):

            if a in s_to_t and s_to_t[a] != b:
                return False

            if b in t_to_s and t_to_s[b] != a:
                return False

            s_to_t[a] = b
            t_to_s[b] = a

        return True
