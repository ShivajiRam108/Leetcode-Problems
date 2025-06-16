class Solution:
    def get_min_max(self, arr):
        min1 = arr[0]
        for i in arr:
            if i < min1:
                min1 = i
        max1 = arr[0]
        for i in arr:
            if i > max1:
                max1 = i 
        return min1 , max1 
x = Solution()
print(x.get_min_max([1,2,10,19,30]))