class Solution:
    def ModifyGames(self, arr, n):

        xor_result = 0
        for num in arr:
            xor_result ^= num

        
        if xor_result == 0:
            return 1
        else:
            return (n % 2) + 1
        
s1 = Solution()
print(s1.ModifyGames([3, 3, 2]))