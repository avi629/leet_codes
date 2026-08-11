class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        groups = [0] * 37

        for i in range(1, n + 1):

            total = 0
            x = i

            while x > 0:
                total += x % 10
                x //= 10

            groups[total] += 1

        largest = max(groups)
        answer = groups.count(largest)

        return answer