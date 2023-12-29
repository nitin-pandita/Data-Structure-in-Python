class Solution:
    def CommonElementSol(self, A, B, C):

        a = set(A)
        b = set(B)
        c = set(C)

        d =  a.intersection(b)
        e =  d.intersection(c)

        return sorted(list(e))
    
s1 = Solution()
print(s1.CommonElementSol([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))