class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        res = set()
        prev = set()
        for i in arr:
            cur = set()
            cur.add(i)
            for j in prev:
                cur.add(j | i)
            for k in cur:
                res.add(k)
            prev = cur
        return len(res) 
x = Solution()
print(x.subarrayBitwiseORs([1,1,2]))  # 3
print(x.subarrayBitwiseORs([0]))    # 1
print(x.subarrayBitwiseORs([1,2,4])) # 6 
