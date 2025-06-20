class Solution:
    def findDuplicates(self, arr):
        res = []
        set1 = set()
        for i in arr:
            if i in set1:
                res.append(i)
            else:
                set1.add(i)
        return res
x = Solution()
print(x.findDuplicates([2, 3, 1, 2, 3]))

#  (Or)

class Solution:
    def findDuplicates(self, arr):
        res = []
        dup = []
        for i in arr:
            if i not in res:
                res.append(i)
            else:
                dup.append(i)
        return dup
x = Solution()
print(x.findDuplicates([2, 3, 1, 2, 3]))