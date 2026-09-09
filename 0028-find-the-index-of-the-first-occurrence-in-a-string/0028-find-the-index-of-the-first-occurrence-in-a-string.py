class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        return -1

##################################################

        # n= len(haystack)
        # m= len(needle)

        # for i in range(n-m+1):
        #     match = True

        #     for j in range(m):
        #         if haystack[i+j] != needle[j]:
        #             match = False
        #             break
            
        #     if match:
        #         return i

        # return -1

        
        