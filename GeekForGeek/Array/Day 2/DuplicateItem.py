class Solution:
    def Duplicate(self, arr):
        n = len(arr)
        repeated = []

        for i in range(n):
            k = i + 1
            for j in range(k, n):
                if arr[i] == arr[j] and arr[i] not in repeated:
                    repeated.append(arr[i])
        
        return repeated
    
s1 = Solution()
print(s1.Duplicate([0,3,3,1,2]))
