class Solution:
    def binarysearch(self, arr, k):
        left = 0 
        right = len(arr) - 1
        res = - 1
        while left <= right:
            mid = left + (right - left ) // 2
            if arr[mid] == k:
                mid = res 
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return res 
x = Solution()
print(x.binarysearch([1,2,3,4,5],4))


#  (or)

def binarysearch(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right ) // 2
        if arr[mid] == k:
            return mid 
        elif arr[mid] < k:
            left = mid - 1
        else:
            right = mid + 1
    return - 1

print(binarysearch([1,2,3,4,5,6], 4))
