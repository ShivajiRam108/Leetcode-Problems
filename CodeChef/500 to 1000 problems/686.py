'''
X Jumps
-----------
-> Chef is currently standing at stair 0 and he wants to reach stair numbered X.
-> Chef can climb either Y steps or 1 step in one move.
-> Find the minimum number of moves required by him to reach exactly the stair numbered X.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single line of input containing two space separated integers X and 
-> Y denoting the number of stair Chef wants to reach and the number of stairs he can climb in one move.

Output Format
----------------
-> For each test case, output the minimum number of moves required by him to reach exactly the stair numbered X.

sample:-
input               output
4
4 2                    2
8 3                    4
3 4                    3
2 1                    2
'''

# Answer 
n = int(input())
for i in range(n):
    a , b = map(int, input().split())
    res = (a // b) + (a % b)
    print(res)