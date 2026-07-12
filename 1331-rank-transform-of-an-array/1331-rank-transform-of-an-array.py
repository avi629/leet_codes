class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        sorted_arr = sorted(arr)
        result = []
        mapping = {}
        rank = 1
        mapping[sorted_arr[0]] = rank

        for i in range(1 , len(sorted_arr)):
            if sorted_arr[i] != sorted_arr[i-1]:
                rank += 1
            mapping[sorted_arr[i]] = rank


        for num in arr:                 # final output array
            result.append(mapping[num])

        return result
            