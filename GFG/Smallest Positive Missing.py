class Solution:
    def missingNumber(self, arr):
        res = []
        for i in arr:
            if i > 0 :
                res.append(i)
        i = 1 
        while True:
            found = False
            for j in res:
                if j == i:
                    found = True
                    break 
            if not found:
                return i 
                break 
            i += 1
x = Solution()
print(x.missingNumber([2, -3, 4, 1, 1, 7])) # 3
print(x.missingNumber( [5, 3, 2, 5, 1])) # 4
print(x.missingNumber([-8, 0, -1, -4, -3]))  # 1 