class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zero_count = 0
        for num in arr:
            if num == 0:
                zero_count += 1
        
        left = len(arr) - 1
        right = len(arr) - 1 + zero_count

        while left >= 0:
            if arr[left] == 0:
                if right < len(arr):
                    arr[right] = 0

                if right - 1 < len(arr):
                    arr[right - 1] = 0

                left -= 1
                right -= 2

            else:

                if right < len(arr):
                    arr[right] = arr[left]

                left -= 1
                right -= 1