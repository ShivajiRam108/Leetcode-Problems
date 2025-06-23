'''
Reach fast
----------
-> Chef is standing at coordinate A while Chefina is standing at coordinate B.
-> In one step, Chef can increase or decrease his coordinate by at most K.
-> Determine the minimum number of steps required by Chef to reach Chefina.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of three integers A,B, and K
-> the initial coordinate of Chef, the initial coordinate of Chefina and the maximum number of coordinates Chef can move in one step.

Output Format
-------------
-> For each test case, output the minimum number of steps required by Chef to reach Chefina.

Sample :- 

input               output 
4
10 20 3               4
36 36 5               0
50 4 100              1
30 4 2                13
'''

# Answer
def reach_fast(test_cases):
    res = []
    for a, b, k in test_cases:
        distance = abs(b - a)
        step = (distance + k - 1) // k
        res.append(step)
    return res

# Input
T = int(input())
test_cases = []
for _ in range(T):
    x, y, z = map(int, input().split())
    test_cases.append((x, y, z))

# Function call
res = reach_fast(test_cases)

# Output
for j in res:
    print(j)
