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


#  using two pointers approach
def isPerfact(arr):
    left = 0
    right = len(arr) -1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    if arr == arr:
        return True
    else:
        return False
print(isPerfact([1,2,3,4,5]))
print(isPerfact([1,2,3,2,1]))

# (Or) using python slicing

class Solution:
    def isPerfect(self, arr: List[int]) -> bool:
        return arr == arr[::-1]
    
x = Solution()
print(x.isPerfect([1,2,3,4,5]))
print(x.isPerfect([1,2,3,2,1]))