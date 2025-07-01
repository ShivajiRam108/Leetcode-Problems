class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res = []
        for i in range(1, n+1):
            if i % 2 == 0:
                res.append(i)
        if n <= 1:
            return 2
        elif n % 2 == 0:
            return n 
        else:
            return n * min(res)
        
x = Solution()
print(x.smallestEvenMultiple(5))
print(x.smallestEvenMultiple(6))
print(x.smallestEvenMultiple(1))

# (Or)

import math
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return math.lcm(2,n)
print(x.smallestEvenMultiple(5))
print(x.smallestEvenMultiple(6))
print(x.smallestEvenMultiple(1))