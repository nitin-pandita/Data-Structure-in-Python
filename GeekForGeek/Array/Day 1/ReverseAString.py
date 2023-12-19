class Solution:
    def reverseWord(self, str:str) -> str:
        reversed_str = str[::-1]
        # starting from the last index and  going to the first index
        return reversed_str

    def reverseWord2(self, str:str) -> str:
        reversed_str = ''.join(reversed(str))
        return reversed_str

s1 = Solution()

print(s1.reverseWord("Geeks"))
print(s1.reverseWord2("nitin"))
