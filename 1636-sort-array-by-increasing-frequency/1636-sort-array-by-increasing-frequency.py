class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Part 1: Count the frequency of each value in nums
        freq = {}
        for arr in nums:
            if arr in freq:           
                freq[arr] += 1
            else:
                freq[arr] = 1

        # Part 2: Sort (value, count) pairs by count ascending,
        # and by value descending when counts are tied
        def sort_key(pair):
            value, count = pair
            return (count, -value)

        sorted_items = sorted(freq.items(), key = sort_key)
        
        # Part 3: Build the final flat array by repeating each
        # value 'count' times, in the sorted order
        result = []
        for value, count in sorted_items:
            for _ in range(count):
                result.append(value)

        return result

########################################################

        