class Solution:
    def NextPerm(self,arr):
        for i in range(len(arr) -1,0, -1):
            if arr[i - 1] < arr[i]:
                arr[i:] = sorted(arr[i:])

                # get the element before the peak element
                j = i - 1

                # swapping the pre-last index with the value
                for k in range(i, len(arr)):
                    arr[k], arr[j] = arr[j], arr[k]
                    return arr
        
        return arr.reverse()
    
s1 = Solution()
print(s1.NextPerm([1,1,5]))