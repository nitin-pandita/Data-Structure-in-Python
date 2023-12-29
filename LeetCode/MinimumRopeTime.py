class Solution:
    def MinTimeOfRope(self,colors, needTime):
        TimeTaken = 0
        i = 0
        j = 0
        while i < len(needTime) and j < len(needTime):
            # they will be used to calculate the time for each ballon
            currTotal = 0
            currMax = 0
# inner loop is responsible for finding the consecutive ballon

            while j < len(needTime) and colors[i] == colors[j]:
                currTotal += needTime[j]
                currMax = max(currMax, needTime[j])
                j +=1

            TimeTaken += currTotal - currMax
            i = j
        
        return TimeTaken
    
s1 = Solution()
print(s1.MinTimeOfRope("aabaa", [1,2,3,4,1]))
