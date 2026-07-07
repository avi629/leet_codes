class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # m = len(num1)
        # n = len(num2)
        # pos = [0] * (m+n)

        # for i in range(m-1 , -1 , -1):
        #     for j in range(n-1, -1 , -1):
        #         # mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        #         mul = int(num1[i]) * int(num2[j])
        #         p1 = i + j
        #         p2 = i + j + 1
        #         total = mul + pos[p2]

        #         pos[p2] = total % 10
        #         pos[p1] += total // 10

        # result = ''.join(str(d) for d in pos).lstrip('0')
        # return result or '0'

############################################################
        m = len(num1)
        n = len(num2)
        pos = [0] * (m+n)

        for i in range(m-1 , -1 , -1):
            for j in range(n-1, -1, -1):

                mul= int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                total = mul  + pos[p2]

                pos[p2] = total % 10
                pos[p1] += total // 10
        
        result = ''.join(str(d) for d in pos).lstrip('0')
        return result or '0'

