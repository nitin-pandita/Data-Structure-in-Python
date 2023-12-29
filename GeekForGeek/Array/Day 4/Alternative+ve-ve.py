class Solution:
    def alternative(self,arr,n):
        pos = [x for x in arr if x > 0] # for getting the +ve 
        neg = [x for x in arr if x < 0] # for getting -ve 
        res = []

        i, j = 0, 0

        while i < len(pos) and j < len(neg):
            res.append(pos[i])
            i += 1
            res.append(neg[j])
            j += 1

        while i < len(pos):
            res.append(pos[i])
            i += 1

        while j < len(neg):
            res.append(neg[j])
            j += 1

        for k in range(len(res)):
            arr[k] = res[k]

        return res

s1 = Solution()
print(s1.alternative([9,4,-2,-1,5,0,-5,-3,2],9))