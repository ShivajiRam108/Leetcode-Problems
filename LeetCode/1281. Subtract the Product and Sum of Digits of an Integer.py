class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_num = 0 
        mul_num =  1
        for i in str(n):
            sum_num += int(i) 
            mul_num *= int(i) 
        return mul_num - sum_num 
x = Solution()
print(x.subtractProductAndSum(234)) #  15 
print(x.subtractProductAndSum(4421)) # 21