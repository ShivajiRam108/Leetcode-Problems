class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1
        while l<r:
            s[l],s[r] = s[r], s[l]
            l+=1
            r-=1
x = Solution()
s = ["h","e","l","l","o"]
x.reverseString(s)
print(s)