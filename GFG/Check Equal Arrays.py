class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        if len(res1) != len(res2):
            return False 
        
        res1 = {}
        res2 = {}
        for i in a:
            if i in res1:
                res1[i] += 1
            else:
                res1[i] = 1
        for j in b:
            if j in res2:
                res2[j] += 1
            else:
                res2[j] = 1 
        
        return res1 == res2
x = Solution()
print(x.checkEqual([1, 2, 5, 4, 0],[2, 4, 5, 0, 1]))
print(x.checkEqual([1, 2, 5],[2, 4, 15]))

    
#  (Or)

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        if len(a) != len(b):
            return False
        return a == b 
x = Solution()
print(x.checkEqual([1, 2, 5, 4, 0],[2, 4, 5, 0, 1]))
print(x.checkEqual([1, 2, 5],[2, 4, 15]))

#  (Or)

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        return sorted(a) == sorted(b)
x = Solution()
print(x.checkEqual([1, 2, 5, 4, 0],[2, 4, 5, 0, 1]))
print(x.checkEqual([1, 2, 5],[2, 4, 15]))