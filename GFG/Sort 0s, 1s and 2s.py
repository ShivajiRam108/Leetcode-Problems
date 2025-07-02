class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        left = 0
        mid = 0 
        right = len(arr) -1 
        while mid <= right:
            if arr[mid] == 0:
                arr[left], arr[mid] = arr[mid] , arr[left]
                left += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid] , arr[right] = arr[right], arr[mid]
                right -= 1
        return arr 
x = Solution()
print(x.sort012([1,2,0,0,1,2]))


#  (Or)
class Solution:
    def sort012(self, arr):
        res = sorted(arr)
        return res
x = Solution()
print(x.sort012([0, 1, 2, 0, 1, 2]))

#  (Or)

class Solution:
    def sort012(self, arr):
        a = []
        b = []
        c = []
        for i in arr:
            if i == 0:
                a.append(i)
            elif i == 1:
                b.append(i)
            else:
                c.append(i)
        return (a + b + c)
    
x = Solution()
print(x.sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))

#  (Or)

class Solution:
    def sort012(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
x = Solution()
print(x.sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))