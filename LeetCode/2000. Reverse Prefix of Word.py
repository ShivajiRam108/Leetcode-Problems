class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        count = 0
        for i in range(1, len(word)):
            if word[i] == ch:
                count = i
                break 
        res = word[0:count+1] [::-1] + word[count +1 :]
        return res 
x = Solution()
print(x.reversePrefix("abcdefd","d"))