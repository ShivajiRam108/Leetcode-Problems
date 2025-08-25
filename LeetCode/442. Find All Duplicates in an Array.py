class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        dup = []
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                dup.append(i)
        return dup 
x = Solution()
print(x.findDuplicates([4,3,2,7,8,2,3,1]))  # Output: [2,3]
print(x.findDuplicates([1,1,2]))  # Output: [1]
print(x.findDuplicates([1]))  # Output: []
print(x.findDuplicates([2,2]))  # Output: [2]