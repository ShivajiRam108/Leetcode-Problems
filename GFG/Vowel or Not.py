class Solution:
    def isVowel (ob,c):
        vowel = 'aeiouAEIOU'
        for i in c:
            if i in vowel:
                return "YES"
        return "NO"
x = Solution()
print(x.isVowel('a'))  # Output: YES
print(x.isVowel('b'))  # Output: NO     
print(x.isVowel('A'))  # Output: YES
print(x.isVowel('B'))  # Output: NO