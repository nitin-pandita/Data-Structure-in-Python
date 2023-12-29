class Solution:
    def MinHeight(self,arr, n , k):
        # sorting the array
        arr.sort()

        # difference between the last and the first element
        diff = arr[-1] - arr[0]

        mx = 0 #finding the max
        mn = 0 #finding the min

        for idx, val in enumerate(arr):
            if idx == 0 or val < k or arr[-1] < k:
            # if any of this condition is true then we are going to skip it
                continue
# Adding k to the next maximum height of tower and subtracting the tallest tower
            mx = max(arr[idx - 1] + k, arr[-1] - k)
            mn = min(arr[0] + k, val - k)

            diff = min(diff, abs(mx - mn))

        return diff

s1 = Solution()
print(s1.MinHeight([1, 5, 8, 10],4,2))
