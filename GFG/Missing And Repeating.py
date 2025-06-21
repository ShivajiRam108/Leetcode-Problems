class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
        x = list(set(arr))
        uniq_sum = sum(x)
        arr_sum = sum(arr)
        dup_ele = arr_sum - uniq_sum
        exp_sum = n * (n + 1) // 2
        mis_ele = exp_sum - (arr_sum - dup_ele)
        res = [dup_ele,mis_ele]
        return res
x = Solution()
print(x.findTwoElement([4, 3, 6, 2, 1, 1]))

#  (Or)
class Solution:
    def findTwoElement( self,arr): 
        min1 = min(arr)
        max1 = max(arr)
        res = []
        for i in range(min1, max1+1):
            if arr.count(i) != 1:
                res.append(i)
        return res 
x = Solution()
print(x.findTwoElement([4, 3, 6, 2, 1, 1]))    