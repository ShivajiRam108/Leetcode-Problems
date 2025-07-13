class Solution:
    def commonElements(self, arr1, arr2, arr3):
        
        return sorted(set(arr1) & set(arr2) & set(arr3))
x = Solution()
print(x.commonElements([1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4]))  # Output: [1, 2, 3]

#  (Or)

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        res = []
        for i in arr1:
            if i in arr2 and i in arr3 and i not in res:
                res.append(i)   
        return sorted(res)
x = Solution()
print(x.commonElements([1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4]))  # Output: [1, 2, 3]
print(x.commonElements([1, 2, 3, 4, 5], [6, 7, 8], [9, 10, 11]))  # Output: []