'''
Reach the Target
-----------------
-> There is a cricket match going on between two teams A and B.
-> Team B is batting second and got a target of X runs. Currently, team B has scored Y runs.
-> Determine how many more runs Team B should score to win the match.

Note: The target score in cricket matches is one more than the number of runs scored by the team that batted first.

Input Format
---------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers X and Y, the target for team B and the current score of team B respectively.

Output Format
-------------
-> For each test case, output how many more runs team B should score to win the match.

Sample:-

input               output

4
200 50                  150
100 99                  1
130 97                  33
53 51                   2
'''

# Answer

N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print(A - B)
