class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # for i in range(len(digits)-1,-1,-1):
        #     if digits[i] == 9:
        #         digits[i] = 0
        #     else:
        #         digits[i] = digits[i] + 1
        #         return digits
        # return [1] + digits
    #  (Or)
        lastDigit = digits.pop()
        addOne = lastDigit + 1
        temp = digits.append(addOne)
        res = []
        for i in digits:
            res.append(i)
        return res
x = Solution()
print(x.plusOne([1,2,3,4]))
