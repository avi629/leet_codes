class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)

        if k == 0:
            return [0] * n

        result = []

        if k > 0:
            curr_sum = sum(code[1:k + 1])

            for i in range(n):
                result.append(curr_sum)

                curr_sum -= code[(i + 1) % n]
                curr_sum += code[(i + k + 1) % n]

        else:
            k = -k

            curr_sum = 0

            for i in range(1, k + 1):
                curr_sum += code[(-i) % n]

            for i in range(n):
                result.append(curr_sum)

                curr_sum -= code[(-k + i) % n]
                curr_sum += code[i % n]

        return result