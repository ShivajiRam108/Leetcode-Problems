'''
Good Investment or Not
-----------------------
-> Chef has invested his money at an interest rate of X percent per annum while the current inflation rate is Y percent per annum.
-> An investment is called good if and only if the interest rate of the investment is at least twice of the inflation rate.
-> Determine whether the investment made by Chef is good or not.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two integers X and Y, the interest rate and the current inflation rate respectively.

Output Format
--------------
-> For each test case, output YES if the investment is good, NO otherwise.
-> You can output any letter in any case. For example YES, yes, yES are all considered same.

Sample :- 

input                   output 
5
7 4                       No
6 3                       Yes
2 4                       No
10 10                     NO
20 1                      Yes
'''

#Answer

N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    res = X // 2
    if res >= Y:
        print("Yes")
    else:
        print("No")
        