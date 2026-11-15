class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # i = len(num1)-1
        # j = len(num2)-1
        # carry = 0
        # ans = ""

        # while i >= 0 or j >=0 or carry:
        #     a = int(num1[i]) if i >= 0 else 0
        #     b = int(num2[j]) if j >= 0 else 0

        #     s = a + b + carry
        #     ans = str(s % 10) + ans
        #     carry = s // 10

        #     i -= 1
        #     j -= 1

        # return ans

#######################################################
        i = len(num1) -1
        j = len(num2) -1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0 or carry:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0

            s = a + b + carry
            ans = str(s % 10) + ans
            carry = s // 10

            
            i -= 1
            j -= 1

        return ans