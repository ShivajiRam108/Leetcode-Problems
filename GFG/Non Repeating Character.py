class Solution:
    def nonRepeatingChar(self,s):
        res = {}
        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for i, j in res.items():
            if j == 1:
                return i 
                break 
        return "$"
    
# (Or)
class Solution:
    def nonRepeatingChar(self,s):
        res = ''
        for i in s:
            if s.count(i) == 1:
                return i 
        return "$"