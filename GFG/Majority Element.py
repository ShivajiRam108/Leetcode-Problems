class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        for i in range(n):
            count = 0 
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1
            if count > n //2 :
                return arr[i]
        return -1 
x = Solution()
print(x.majorityElement([1, 1, 2, 1, 3, 5, 1]))  # 1
print(x.majorityElement([7])) # 7
print(x.majorityElement([2, 13])) # -1

# (Or)

class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        count = 0 
        ele = None 
        for i in range(n):
            if count == 0 :
                count = 1 
                ele = arr[i]
            elif ele == arr[i]:
                count += 1
            else:
                count -= 1

        count1 = 0 
        for i in range(n):
            if arr[i] == ele:
                count1 += 1
        if count1 > n // 2:
            return ele 
        return -1 
x = Solution()
print(x.majorityElement([1, 1, 2, 1, 3, 5, 1]))  # 1
print(x.majorityElement([7])) # 7
print(x.majorityElement([2, 13])) # -1