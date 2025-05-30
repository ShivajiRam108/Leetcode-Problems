'''
Power of Four
--------------
-> Given an integer n, return true if it is a power of four. Otherwise, return false.
-> An integer n is a power of four, if there exists an integer x such that n == 4x.

sample :- 
------------
input                   output
------                 -------

16                         true
5                          false 
1                          true 


'''

#  Answer 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1