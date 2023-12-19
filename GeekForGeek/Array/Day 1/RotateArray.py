class Solution:
    def rotate(self,arr):

        l = arr[-1] # for getting the last element in the array
        # remove the last element in the array
        arr.pop()
        arr.insert(0,l)
        return arr
    

s1  = Solution()
print(s1.rotate([23,45,46,7,22,4]))