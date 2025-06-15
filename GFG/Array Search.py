class Solution:
    #Complete the below function
    def search(self,arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i 
        return -1 
x = Solution()
print(x.search([1,2,3,4], 3))