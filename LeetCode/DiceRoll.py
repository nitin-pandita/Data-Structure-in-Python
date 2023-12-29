class Solution:
    def __init__(self):
        self.p = 10** + 7
    def DiceRollSum(self, n,k,target):
        if target < n or target > k *n:
            return 0
        
        if target == 0:
            return 1 if n == 0 else 0
        
        ans = 0
        for i in range(1, k + 1):
            ans = (ans % self.p + self.DiceRollSum(n - 1,k,target - 1)%self.p)%self.p

        return ans
    
s1 = Solution()
print(s1.DiceRollSum(2,6,12))
