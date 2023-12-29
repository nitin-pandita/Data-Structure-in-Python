class Solution:
    def DeterMatrix(self, matrix, n):
        # if there is only one element then return the first index of the matrix
        if n == 1:
            return matrix[0][0]
        
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        
        deter = 0

        # now for matrix greater than 2
        for i in range(n):
            minor_mat = [row[:i] + row[i + 1 : ] for row in matrix[1:]]
            cofac = matrix[0][i] * ((-1) ** i)
            deter += cofac * self.DeterMatrix(minor_mat,n -1)
        return deter
    
s1 = Solution()
print(s1.DeterMatrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 10, 9]
], 3))