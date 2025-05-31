class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # return num in [6,28, 496, 8128, 33550336]

        # (Or) 
        
        if num == 1:
            return False
        res = 1
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                res  += i + num // i 
        return num == res


