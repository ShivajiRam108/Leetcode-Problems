class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            res += 1
        return res
    
x = Solution()
print(x.numberOfSteps(14))

#     (Or)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num != 0:
            res += 1
            if num & 1:
                num -= 1
            else:
                num >>= 1 
        return res
x = Solution()
print(x.numberOfSteps(8))

    # # (Or)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() -1 + num.bit_count()
x = Solution()
print(x.numberOfSteps(123))