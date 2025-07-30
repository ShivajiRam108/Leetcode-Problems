class Solution:
    def countSegments(self, s: str) -> int:
        res = s.split()
        return len(res)
x = Solution()
print(x.countSegments("Hello, my name is John"))  # 5
print(x.countSegments("Hello")) # 1