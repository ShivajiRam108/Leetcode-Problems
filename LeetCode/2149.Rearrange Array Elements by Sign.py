class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res = [0]* len(nums)
        pos = 0
        neg = 1
        for i in nums:
            if i > 0:
                res[pos] = i
                pos +=2
            else:
                res[neg] = i
                neg +=2
        return res
        # pos = [i for i in nums if  i > 0]
        # neg = [ i for i in nums if i < 0]
        # res = []
        # i, j= 0, 0
        # while i < len(pos) and j < len(neg):
        #     res.append(pos[i])
        #     res.append(neg[j])
        #     i, j = i+1, j+1
        # return res