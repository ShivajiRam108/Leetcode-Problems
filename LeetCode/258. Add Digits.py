class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0 
        elif num % 9 == 0:
            return 9 
        else:
            return num % 9 
x = Solution()
print(x.addDigits(38))  # 2
print(x.addDigits(0))  # 0 
print(x.addDigits(9))  # 9

# (or)

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num 
        if num % 9 != 0:
            return num % 9 
        if num % 9 == 0:
            return 9 
x = Solution()
print(x.addDigits(38))  # 2
print(x.addDigits(0))  # 0 
print(x.addDigits(9))  # 9