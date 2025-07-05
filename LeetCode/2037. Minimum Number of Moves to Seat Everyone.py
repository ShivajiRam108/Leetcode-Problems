class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        res = 0 
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res 
    
x = Solution()
print(x.minMovesToSeat([3,1,5], [2,7,4]))
print(x.minMovesToSeat([4,1,5,9], [1,3,2,6]))
print(x.minMovesToSeat([2,2,6,6],[1,3,2,6]))