class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        mat = [sorted(item) for item in grid]
        n = len(grid[0])
        for j in range(0 , n):
            ele = max([row[n-1-j] for row in mat])
            result = result + ele
        
        return result