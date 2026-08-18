class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        freq = {}
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in arr2:
            result.extend([num] * freq[num])

        set1 = set(freq.keys())
        set2 = set(arr2)
        res = sorted(set1 - set2)

        for num in res:
            result.extend([num] * freq[num])
        
        return result

        