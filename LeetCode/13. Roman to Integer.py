class Solution:
    def romanToInt(self, s: str) -> int:
        # res = 0
        # roman = {
        #     "I" : 1,"V": 5,"X": 10, "L": 50,"C": 100,"D": 500, "M" : 1000
        # }
        # for i, j in zip(s, s[1:]):
        #     if roman[i] < roman [j]:
        #         res -=roman[i]
        #     else:
        #         res +=roman[i]
        # return res + roman[s[-1]]
        
        # (Or)
# using two pointers 
        left = 0 
        right = 1
        total = 0
        roman = {"I" : 1,"V": 5,"X": 10, "L": 50,"C": 100,"D": 500, "M" : 1000}
        while left < len(s)-1:
            if roman[s[left]] < roman[s[right]]:
                total -= roman[s[left]]
            else:
                total += roman[s[left]]
            left += 1
            right += 1
        total += roman[s[left]]
        return total 
    
x = Solution()
print(x.romanToInt("MCMXCIV"))
