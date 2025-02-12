class Solution:
    def findSubsequences(self, nums: list[int]) -> list[List[int]]:
        res = []

        def dfs(index, path):
            if len(path) >= 2:
                res.append(path[:])
            seen = set()
            for i in range(index, len(nums)):
                if nums[i] in seen:
                    continue
                if not path or nums[i] >= path[-1]:
                    seen.add(nums[i])
                    dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return res

# Example usage
solution = Solution()
print(solution.findSubsequences([4,6,7,7]))


#  (Or)
class Solution:
    def findSubsequences(self, nums:list[int]) -> list[List[int]]:
        ans = set()
        n = len(nums)
        def solve(s,arr):
            if len(arr)>1:
                ans.add(tuple(arr))
            for i in range(s,n):
                if not arr or arr[-1]<=nums[i]:
                    solve(i+1,arr+[nums[i]])
                else:
                    solve(i+1,arr)
        solve(0,[])
        return list(map(list,ans))