class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current = []
        index = 0
        def backtrack(index , remaining):
            if remaining == 0:
                result.append( current[:] )
                return

            if remaining < 0 or index == len(candidates):
                return
            
            # Take the current candidate
            current.append(candidates[index])

            backtrack(index, remaining - candidates[index])

            current.pop()

            # Skip the current candidate
            backtrack(index + 1, remaining)

        backtrack(0, target)

        return result