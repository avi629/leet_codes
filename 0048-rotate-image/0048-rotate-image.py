class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):  # swap with column with rows
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:      
            row.reverse()       # reverse each row

#####################################
        # return list(zip(*matrix[::-1])) # creates a new matrix

######################################3

        # for i in range(len(matrix)):
        #     for j in range(i+1, len(matrix)):  # swap with column with rows
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for row in matrix:      
        #     row.reverse()       # reverse each row