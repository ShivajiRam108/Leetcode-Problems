class Solution:
    def firstRep(self, s):
        res = {}
        for i in s:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        for key, value in res.items():
            if value > 1:
                return key 
            else:
                continue 
        return -1 
    
x = Solution()
print(x.firstRep("geeksforgeeks"))  # Output: 'g'
print(x.firstRep("hello"))  # Output: 'l'
print(x.firstRep("abcde"))  # Output: -1

# (Or) 
class Solution:
    def firstRep(self, s):
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return -1
    
x = Solution()
print(x.firstRep("geeksforgeeks"))  # Output: 'g'
print(x.firstRep("hello"))  # Output: 'l'



