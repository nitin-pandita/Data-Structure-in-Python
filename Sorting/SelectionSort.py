class Solution:
    def findSmallestIndex(self, arr):
        smallest = arr[0]
        smallest_index = 0

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        
        return smallest_index

    
    def Selection(self, arr):
        # created a new array for storing the sorted values
        new_arr = []
# with the help of this I will get teh smallest element
        for i in range(0, len(arr)):
            smallest = self.findSmallestIndex(arr)
            # we are removing the element from the main array and storing it in the new array
            new_arr.append(arr.pop(smallest))

        return new_arr
    
s1 = Solution()

print(s1.Selection([5,3,6,2,10]))


