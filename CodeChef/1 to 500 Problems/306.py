'''
Chef and Donation
------------------
-> In a certain month, Chef earned X rupees while Chefina earned Y rupees such that Y>X.
-> Since they want to end up with exactly the same amount, they decide to donate the difference between their income to a charity.

=> Find the amount they donate in the month.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers X and Y — the income of Chef and Chefina in a month, respectively.

Output Format
--------------
-> For each test case, output on a new line, the amount they donate in the month.

Sample:-

input                   output
4
1 3                       2
2 5                       3
4 5                       1
2 10                      8
'''

# Answer
N = int(input())
for i in range(N):
    X  , Y = map(int, input().split())
    print(Y - X)

#  Another way
N = int(input())
for i in range(N):
    X , Y = map(int, input().split())
    res = 0
    if Y > X:
        res += ( Y - X)
    print(res)