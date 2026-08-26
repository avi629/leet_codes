class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        left = 0
        curr_sum = 0

        for right in range(len(arr)):
            curr_sum += arr[right]

            if right - left +1 == k:
                if curr_sum >= k * threshold:
                    count += 1
                
                curr_sum -= arr[left]
                left += 1

        return count


        