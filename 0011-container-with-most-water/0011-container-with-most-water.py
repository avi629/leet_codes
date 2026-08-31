class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # left = 0
        # right = len(height) - 1
        # max_water = 0

        # while left < right:
        #     h = min(height[left], height[right])
        #     w = right - left
        #     area = h * w
        #     max_water = max(max_water, area)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return max_water

############################################################

        left = 0
        right = len(height)-1
        max_water = 0

        while left < right:
            area = min(height[left] , height[right]) * (right - left)
            # water = shorter wall × distance between walls

            max_water = max(max_water , area)
        
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

        