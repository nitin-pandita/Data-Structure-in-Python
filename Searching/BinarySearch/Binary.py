# What is binary search: Binary Search is a searching algorithm that is used to reduce the number of step in searching the element in the array. It is calculated by taking the mid element and adjusting the low and high accordingly

#? Logarithmic Time : Normal Algorithm Will take linear amount of time that will be "O(n)" where as Binary Search will take Logarithmic Time which means O(log n)
class BinarySearch:
    def BinarySearchAlgo(self, arr, item):
        low = 0
        high = len(arr)
        

        while (low <= high):
            # finding the middle element
            mid =round((low + high)/2)
            guess = arr[mid]

            if guess == item:
                return mid
            elif guess > item:
                # move the high towards the low
                high = mid - 1
            else:
                # move it towards the high
                low = mid + 1
        return -1
    
s1 = BinarySearch()

print(s1.BinarySearchAlgo([1,3,5,7,9],7))
        
