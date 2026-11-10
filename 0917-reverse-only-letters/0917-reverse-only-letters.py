class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # chars = list(s)
        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     if chars[left].isalpha() and chars[right].isalpha():
        #         chars[left] , chars[right] = chars[right] , chars[left]
        #         left += 1
        #         right -= 1
            
        #     elif not chars[left].isalpha():
        #         left += 1
            
        #     else:
        #         right -= 1

        # return "".join(chars)

###################################################################
        chars = list(s)
        left = 0 
        right = len(s) - 1

        while left < right:
            if chars[left].isalpha() and chars[right].isalpha():
                chars[left] , chars[right] = chars[right] , chars[left]
                left += 1
                right -= 1

            elif not chars[left].isalpha():
                left += 1
            else:
                right -= 1

        return "".join(chars)

        