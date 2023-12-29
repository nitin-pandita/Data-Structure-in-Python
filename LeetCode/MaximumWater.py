# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# ? we are going to find the length and breadth of the blocks and return the maximum one
class Solution:
    def MaxHeight(self, arr):
        maxArea = 0
        for a in range(len(arr)):
            for b in range(len(arr)):
                length = min(arr[a], arr[b])
                breadth = b - a
                area = length * breadth
                maxArea = max(maxArea, area)

        return maxArea
    
    # *  for the optimal solution
    def OptimalSolution(self, arr):
        p1 = 0
        p2 = len(arr) - 1
        maxArea = 0
        while(p1 <= p2):
            length = min(arr[p1], arr[p2])
            width = p2 - p1
            area = length * width
            maxArea = max(maxArea, area)

            if arr[p1] <= arr[p2]:
                p1 += 1
            else:
                p2 -=1

        return maxArea
s1 = Solution()
print(s1.OptimalSolution([1,8,6,2,5,4,8,3,7]))