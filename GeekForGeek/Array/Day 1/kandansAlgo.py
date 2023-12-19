class Solution:
    def KadansAlgo(self, arr, n):
        curr = 0
        maxSum = arr[0]

        for i in range(0, n):
            # adding the elements
            curr = curr + arr[i]
            # if that sum is greater than the current maxSum then update the maxSum
            if maxSum < curr:
                maxSum = curr
            # if the value was less than the 0 then reset the value of curr to 0
            if curr < 0:
                curr = 0

            # at last we wil have the max sum element and we are going to return it..
        return maxSum
s1 = Solution()
print(s1.KadansAlgo([1, 2, 3, -2, 5],5))