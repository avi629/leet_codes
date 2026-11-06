class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i = 0
        # j = 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1

        # return i == len(s)

###############################################
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

#############################################

        # matched = 0
        # prev = 0
        # for i in range(len(s)):
        #     for j in range(prev , len(t)):
        #         if s[i] == t[j]:
        #             matched += 1
        #             prev = j+1
        #             break
        
        # return matched == len(s)
        