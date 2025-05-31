'''
Minimum number of coins
----------------------
-> Chef has infinite coins in denominations of rupees 5 and rupees 10.
-> Find the minimum number of coins Chef needs, to pay exactly X rupees. 
-> If it is impossible to pay X rupees in denominations of rupees 5 and 10 only, print −1.

Input Format
-------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> Each test case contains of a single integer X.

Output Format
-------------
-> For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactly X rupees. 
-> If it is impossible to pay X rupees in denominations of rupees 5 and 10 only, print −1.

Sample:-

input                   output

3
50                          5
15                          2
8                           -1
'''

# Answer
N = int(input())
for i in range(N):
    A = int(input())
    if A % 5 != 0:
        print(-1)
    else:
        X = A // 10 
        res = A % 10 
        if res == 0:
            print(X)
        else:
            print(X+1)


