class Solution:
    def UnionOfArray(self, a, b):
        #* creating a new set and storing the value of the both array and concentering it !!
        return set(a + b)
    


s1 = Solution()
print(s1.UnionOfArray([45,34,23,23,23,2], [23,4,5,12,121]))

