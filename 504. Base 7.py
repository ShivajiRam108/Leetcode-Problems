class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []  
        sign = 1 if num >= 0 else -1
        num = abs(num) 
        while num > 0:
            res.append(str(num % 7))
            num //= 7 
        result = ''.join(reversed(res))
        return '-' + result if sign == -1 else result
    
# (Or)
# Take input from the user
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []  
        sign = 1 if num >= 0 else -1
        num = abs(num) 
        while num > 0:
            res.append(str(num % 7))
            num //= 7 
        result = ''.join(reversed(res))
        return '-' + result if sign == -1 else result

num = int(input("Enter a number: "))
sol = Solution()
result = sol.convertToBase7(num)
print("Base 7 representation:", result)