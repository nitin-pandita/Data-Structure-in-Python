class Solution:
    def CountPairsSum(self, arr, k):
        # empty dictionary
        
        d = {}
        count = 0 

        for i in arr:
            complement = k - i
            
            if complement in d:
                count += d[complement]

            if i in d:
                d[i] += 1
            
            else:
                d[i] = 1
        
        return count
    
s1 = Solution()
print(s1.CountPairsSum([1,5,7,1], 6))