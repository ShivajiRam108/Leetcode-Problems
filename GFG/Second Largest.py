class Solution:
    def getSecondLargest(self, arr):
        res = list(set(arr))
        if len(res) < 2:
            return -1
        res.sort()
        return res[-2]
x = Solution()
print(x.getSecondLargest([10, 5, 10]))

#  (Or) but in this case some test case is wrong.it will be take more time that why it is wrong.

class Solution:
    def getSecondLargest(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        for i in range(len(res)):
            for j in range(len(res)-i-1):
                if res[j] > res[j+1]:
                    res[j], res[j+1] = res[j+1] , res[j]
        return res[j - 2]