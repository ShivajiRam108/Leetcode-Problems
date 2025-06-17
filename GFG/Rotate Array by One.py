class Solution:
    def rotate(self, arr):
        last_value = arr.pop() # accsesing the last index 
        arr.insert(0,last_value) # adding the last number in frist in a array.
        res = []
        for i in arr:
            res.append(i)
        return res
    
x = Solution()
print(x.rotate([1, 2, 3, 4, 5]))