class Solution:
    def KthSmallestElement(self,arr,l,r,k):

        result = arr.sort()

        return arr[k -1]
    
    def Approach2(self, arr, l, r, k):
        new_arr = []
        for i in arr:
            new_arr.append(i)
            new_arr.sort(reverse=True)
        n = k* - 1
        return new_arr    
s1 = Solution()
print(s1.Approach2([5,7,12,2,12,6], 0 , 5, 2))
print(s1.KthSmallestElement([7, 10 ,4 ,3, 20 ,15], 0,5,3))

