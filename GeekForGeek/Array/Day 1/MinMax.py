class Solution:
    def MinMax(self,a, n):
        min = a[0]
        max = a[0]

        for i in range(n):
            if a[i] < min:
                min = a[i] # wil help in finding the min element
            elif a[i] > max:
                max = a[i]

        return min,max
    
s1 = Solution()
print(s1.MinMax([3, 2, 1, 56, 10000, 167], 6))
