class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        left = 1
        right = position[-1] - position[0]

        while left <= right:
            mid = (left + right) // 2

            balls = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    balls += 1
                    last_position = position[i]

            if balls >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans