class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len -1 , -1 , -1):
            total = carry + int(a[i]) + int(b[i])
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        result.reverse()
        return ''.join(result)