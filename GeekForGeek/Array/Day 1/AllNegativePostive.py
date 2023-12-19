class Solution:
    def NegativePositive(self,arr,n):
        arr1 = []
        arr2 = []

        for i in arr:
            if i < 0:
                arr1.append(i)
            else:
                arr2.append(i)
            
        arr3 = arr2 + arr1

        # for i in range(n):
        #     arr[i] = arr3[i]

        return arr3

s1 = Solution()
print(s1.NegativePositive([1, -1, 3, 2, -7, -5, 11, 6 ],8))
