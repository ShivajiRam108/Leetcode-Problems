class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_n = 0
        mul = 1
        for i in str(n):
            sum_n += int(i)
        for i in str(n):
            mul *= int(i)
        return mul - sum_n