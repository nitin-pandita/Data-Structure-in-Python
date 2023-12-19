def gameOfXor(N, A):
        # if it is divisible by 2 then return 0
        if N % 2 == 0:
            return 0
        
        ans = 0
        for i in range(1, N + 1, 2):
            ans = ans ^ A[i + 1]

        return ans

print(gameOfXor(3, [1,2,3]))