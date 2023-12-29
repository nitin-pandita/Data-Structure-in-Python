class Solution:
    def MinimumJumps(self,arr, n):
        
#  we are at the last index of the array
        # base condition
            steps = 0
            length = len(arr)
            if len(arr) == 1: return 0
            if arr[0] == 0: return -1
            curr = min(arr[0], length - 1)
            mx = curr
            for i in range(0, len(arr)):
                if arr[i] > 0: mx = max(mx, min(arr[i] + i, length - 1))
                if i == curr:
                    steps += 1
                    if curr == mx and mx != length - 1: return -1
                    curr = mx
            return -1 if mx != length - 1 else steps
    
s1 = Solution()
print(s1.MinimumJumps([27, 8 ,8, 7, 22 ,7 ,12 ,30 ,27, 18 ,11 ,24 ,4 ,19, 14 ,26, 25, 21 ,24 ,3 ,10, 26, 6, 27 ,17 ,6 ,29 ],29))
        
