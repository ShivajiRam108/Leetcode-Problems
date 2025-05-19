'''
Candy Distribution
---------------------
-> Chef has N candies. He has to distribute them to exactly M of his friends such that each friend gets equal number of candies and each friend gets even number of candies.
-> Determine whether it is possible to do so.

NOTE: Chef will not take any candies himself and will distribute all the candies.

Input Format
----------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> Each test case contains of a single line of input, two integers N and M, the number of candies and the number of friends.

Output Format
-------------
-> For each test case, the output will consist of a single line containing Yes if Chef can distribute the candies as per the conditions and No otherwise.
-> You may print each character of the string in uppercase or lowercase (for example, the strings yes, Yes, yEs, and YES will all be treated as identical).

sample:-

input                   output
4
9 3                        No
4 1                        Yes
4 2                        Yes
8 3                        No
'''

# Answer 
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    if a % b == 0 and (a // b ) % 2 == 0 :
        print("Yes")
    else:
        print("No")