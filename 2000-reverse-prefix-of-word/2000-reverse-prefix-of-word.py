class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        i = 0
        while word[i] != ch:
            i += 1
        part1 = word[0 : i+1]
        part2 = part1[::-1]
        
        return part2 + word[ i+1: ]