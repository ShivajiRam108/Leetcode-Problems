class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num 
        while low <= high:
            mid = (low + high) //2
            res = mid * mid 
            if res == num:
                return True 
            elif res < num:
                low = mid + 1
            else:
                high = mid - 1
        return False