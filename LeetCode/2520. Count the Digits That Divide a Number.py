class Solution:
    def countDigits(self, num :int) -> int:
        res = 0 
        for i in str(num):
            if int(num) % int(i) == 0:
                res += 1 
        return res 
x = Solution()
print(x.countDigits(7))
print(x.countDigits(121))
print(x.countDigits(1248))