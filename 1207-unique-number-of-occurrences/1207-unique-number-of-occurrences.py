class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for x in arr:
            if x in freq:          # count frequencies using dictonary
                freq[x] += 1
            else:
                freq[x] = 1

        uniq = set(freq.values())   # use set and comare length 
        for num in uniq:            # of uniq with freq.value()
            if len(uniq) == len(freq.values()):
                return True
            else:
                return False
