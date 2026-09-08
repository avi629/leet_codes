class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)- 1

        left_max = 0
        right_max = 0
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]

                right -= 1

        return total 




        ##################################################
        # total = 0

        # for i in range(1, len(height) - 1):
        #     left_max = max(height[:i])
        #     right_max = max(height[i + 1:])

        #     water = min(left_max, right_max) - height[i]
        #     if water > 0:
        #         total += water

        # return total