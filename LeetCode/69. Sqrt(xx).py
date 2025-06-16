class Solution:
    def mySqrt(self, x: int) -> int:
        res = (x ** 0.5)
        n = int(res)
        return n
    
    #  (Or)
        return int(x ** 0.5)
    #  (Or)
        res = math.sqrt(x)
        return int(res)
    # (Or)
        res = pow(x, 0.5)
        return int(res)