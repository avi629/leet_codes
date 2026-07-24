class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # words = s.split()
        # n = len(words)
        # result = [""] * n

        # for word in words:
        #     pos = int(word[-1])
        #     index = pos - 1
        #     clean_word = word[:-1]
        #     result[index] = clean_word

        # return " ".join(result)
        
###################################################
        words = s.split()
        result = [""] * len(words)

        for word in words:
            pos = int(word[-1])
            clean_word = word[ :-1]
            result[pos-1] = clean_word

        return " ".join(result)