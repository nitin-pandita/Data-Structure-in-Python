class Solution:
    def MergeIntervals(self,arr):
        ans = []
        # sorted the array
        arr.sort()

        if len(arr) == 0:
            return ans
        
        temp = arr[0]

        for interval in arr:
            if interval[0] <= temp[1]:
                temp[1] = max(temp[1], interval[1])
            else:
                ans.append(temp)
                temp = interval
        ans.append(temp)

        return ans

s1 = Solution()
print(s1.MergeIntervals([[1,3],[2,6],[8,10],[15,18]]))