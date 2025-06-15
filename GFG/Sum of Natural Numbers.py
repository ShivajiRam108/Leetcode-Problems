class Solution:
    def seriesSum(self, arr : int) -> int:
        total_sum = 0 
        for i in range(1, arr+ 1):
            total_sum += i 
        return total_sum
    

x = Solution()
print(x.seriesSum(5))