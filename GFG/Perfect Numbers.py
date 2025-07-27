class Solution:
    def isPerfect(self, n):
        res = 0 
        for i in range(1, n):
            if n % i == 0 :
                res += i 
        if n == res:
            return True 
        else:
            return False 
x = Solution()
print(x.isPerfect(6)) # True
print(x.isPerfect(10)) # False
print(x.isPerfect(15)) # False
print(x.isPerfect(28))  # True
print(x.isPerfect(496)) # True 
print(x.isPerfect(8128)) # True

# less time in gfg   (Or)

class Solution:
    def isPerfect(self, n):
        # code here 
        
        res = 0 
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                res += i 
                if i != n // i:
                    res += n // i 
        return (res- n  == n)

x = Solution()
print(x.isPerfect(6)) # True
print(x.isPerfect(10)) # False
print(x.isPerfect(15)) # False
print(x.isPerfect(28))  # True
print(x.isPerfect(496)) # True 
print(x.isPerfect(8128)) # True