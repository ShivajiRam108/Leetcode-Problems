#  it is a aptimal code and this is a best algorithm for counting majority element in a list.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0 
        ele = None 
        for i in range(n):
            if count == 0 :
                count = 1
                ele = nums[i]
            elif ele == nums[i]:
                count += 1
            else:
                count -= 1
        count1 = 0 
        for i in range(n):
            if nums[i] == ele:
                count1 += 1
        if count1 > n //2:
            return ele
        return -1 
x = Solution()
print(x.majorityElement([3,2,3]))  #  3
print(x.majorityElement([2,2,1,1,1,2,2]))  # 2 



# (Or)  it will given some error like time limit error.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            count = 0 
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
                
            if count > n // 2:
                return nums[i]
        return - 1
x = Solution()
print(x.majorityElement([3,2,3]))  #  3
print(x.majorityElement([2,2,1,1,1,2,2]))  # 2 
