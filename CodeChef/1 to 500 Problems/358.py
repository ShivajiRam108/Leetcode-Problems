'''
Final Population
------------------
-> There were initially X million people in a town, out of which Y million people left 
-> the town and Z million people immigrated to this town.Determine the final population of town in millions.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of each test case consists of three integers X, Y and Z.

Output Format
--------------
-> For each test case, output the final population of the town in millions.

Sample:- 

input                       output 
4
3 1 2                          4
2 2 2                          2
4 1 8                          11
10 1 10                        19
'''

# Answer 

N = int(input())
for i in range(N):
    X, Y , Z = map(int, input().split())
    res = (X - Y) + Z
    print(res)
    