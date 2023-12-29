class Solution:
    def AntiDiagonalSol(self,matrix):
        result = []
        n = len(matrix)

        for d in range(n + n - 1):
            cd = [] #empty diagonal
            for i in range(max(0, d - n + 1), min(d, n -1) + 1):
                j  = d - i
                cd.append(matrix[i][j])
            result.extend(cd)
        
        return result

s1 = Solution()
print(s1.AntiDiagonalSol([[1,2],[3,4]]))