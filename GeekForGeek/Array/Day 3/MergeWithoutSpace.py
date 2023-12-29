class Solution:
    def MergeSpace(self, arr1, arr2, n, m):
        # here arr1 and arr2 are the two arrays, and n and m are the number of elements in both the arrays respectively

        arr = [0] * (n + m)

        # Copy elements from arr1 and arr2 to arr
        for i in range(n):
            arr[i] = arr1[i]

        for j in range(m):
            arr[j + n] = arr2[j]

        arr.sort()

        # Update arr1 and arr2 from the merged arr
        for i in range(n):
            arr1[i] = arr[i]

        for j in range(m):
            arr2[j] = arr[j + n]

        return arr

s1 = Solution()
result = s1.MergeSpace([10, 12], [5, 18, 20], 2, 3)
print(result)
