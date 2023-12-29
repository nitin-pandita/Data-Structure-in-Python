import sys
class Solution:
    def Stocks(self, arr):
        if len(arr) == 0:
            return 0
        
        minPrice = sys.maxsize
        maxSellingPrice = 0

        for i in range(len(arr)):
            minPrice = min(minPrice, arr[i])
            maxSellingPrice = max(maxSellingPrice,arr[i] - minPrice)

        return maxSellingPrice
    
s1 = Solution()