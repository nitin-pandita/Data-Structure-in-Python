class Solution:
    def numDecoding(self, arr):
        dp = {len(arr): 1}

        def dfs(i):
            # base condition
            if arr[i] == "0":
                return 0
            
            if i in dp:
                return dp[i]
            
            res = dfs(i + 1)

            if(i + 1 < len(arr) and (arr[i + 1] == "1" or arr[i] == "2" and arr[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dp
s1 = Solution()
print(s1.numDecoding("12"))