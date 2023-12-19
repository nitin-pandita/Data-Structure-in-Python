class Solution:
    def postOfRightMostBit(self,m,n):
        # we have to find the rightmost different bit in the binary representation
        if m == n:
            # it means both of them are having same bits
            return -1
        
        M, N , O = 0 , 0 ,1
        while m and n:
            M = m % 2 # used to find the rightmost bit of m
            N = n % 2 # used to find the leftmost bit of n
            m = m // 2 # shifts m to the right by one position
            n = n // 2 # shifts n to the right by one position

            if M != N:
                return O
            O += 1

        return -1


s1 = Solution()
print(s1.postOfRightMostBit(11,9))