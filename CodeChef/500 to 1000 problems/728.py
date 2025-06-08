'''
A or B
----------
-> There are two problems in a contest.Problem A is worth 500 points at the start of the contest.
-> Problem B is worth 1000 points at the start of the contest.
-> Once the contest starts, after each minute:
=> Maximum points of Problem A reduce by 2 points .
=> Maximum points of Problem B reduce by 4 points.
-> It is known that Chef requires X minutes to solve Problem A correctly and Y minutes to solve Problem B correctly.
-> Find the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.

Input Format
---------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> Each test case contains of a single line of input, two integers X and Y - the time required to solve problems A and B in minutes respectively.

Output Format
--------------
-> For each test case, output in a single line, the maximum number of points Chef 
-> can score if he optimally decides the order of attempting both the problems.

Sample 

Input                output

4
10 20                   1360
8 40                    1292
15 15                   1380
20 10                   1400

'''
# Answer
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    a = 500 - 2 * x
    b = 1000 - 4 * y
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    ans1 = a + b
    a = 500 - 2 * y
    b = 1000 - 4 * x
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    ans2 = a + b
    print(max(ans1, ans2))

#  (Or)

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    ans1 = max(0, 500 - 2 * x) + max(0, 1000 - 4 * y)
    ans2 = max(0, 500 - 2 * y) + max(0, 1000 - 4 * x)
    print(max(ans1, ans2))