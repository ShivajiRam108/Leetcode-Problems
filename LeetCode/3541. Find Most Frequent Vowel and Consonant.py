class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {'a', 'i','e','o','u'}
        max_vowel = [0] * 26
        max_consonents = [0] * 26
        for i in s:
            idx = ord(i) - ord('a')
            if i in vowel:
                max_vowel[idx] += 1
            else:
                max_consonents[idx] += 1
        return max(max_consonents) + max(max_vowel)
x = Solution()
print(x.maxFreqSum("successes"))
print(x.maxFreqSum("aeiaeia"))