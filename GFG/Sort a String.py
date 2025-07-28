class Solution:
    def sort(self, s): 
        return ''.join(sorted(s))
x = Solution()
print(x.sort("edcab"))

# (Or)

class Solution:
    def sort(self, s): 
        res = list(s)
        n = len(res)
        for i in range(n):
            for j in range(0,n-i-1):
                if res[j] > res[j+1]:
                    res[j], res[j+1] = res[j+1],res[j]
        return ''.join(res)
x = Solution()
print(x.sort("edcab"))
print(x.sort("xzy"))