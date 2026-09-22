
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title=title.split()
        for i in range(len(title)):
            if len(title[i])<=2:
                title[i]=title[i].lower()
            else:
                word=title[i]
                word=word.lower()
                title[i]=word[0].upper()+word[1:]
        return " ".join(title)
