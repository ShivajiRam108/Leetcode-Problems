class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def helper(dividend, divisor):
            if dividend < divisor:
                return 0
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            return multiple + helper(dividend - temp, divisor)

        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        result = helper(abs(dividend), abs(divisor))
        return -result if negative else result
    
#  ( Or)
# you can write direct  of this 

# return int(divident / divisor)