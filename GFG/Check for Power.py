import math
class Solution:
    def isPowerOfAnother (ob,X,Y):
        if X == 1:
            return Y == 1
        res = math.log(Y) / math.log(X)
        return res == math.floor(res)
x = Solution()
print(x.isPowerOfAnother(2, 8))  # Output: True (2^3 = 8)   
print(x.isPowerOfAnother(3, 9))  # Output: True (3^2 = 9)
print(x.isPowerOfAnother(4, 16))  # Output: True (4^2 = 16)
print(x.isPowerOfAnother(5, 25))  # Output: True (5^2 = 25)
print(x.isPowerOfAnother(2, 10))  # Output: False (2^x != 10 for any integer x)