from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        res = []
        for i in range(len(arr)-1,-1,-1):
            res.append(arr[i])
        if arr == res:
            return True
        else:
            return False
x = Solution()
print(x.isPerfect([1,2,3,4,5]))
print(x.isPerfect([1,2,3,2,1]))


# (Or)

class Solution:
    def isPerfect(self, arr: List[int]) -> bool:
        return arr == arr[::-1]
    
x = Solution()
print(x.isPerfect([1,2,3,4,5]))
print(x.isPerfect([1,2,3,2,1]))