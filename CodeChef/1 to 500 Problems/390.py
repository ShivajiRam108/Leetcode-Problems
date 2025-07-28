'''
Minimum Coins
--------------
-> There are only 2 type of denominations in Chefland:
-> Coins worth 1 rupee each Notes worth 10 rupees eachChef wants to pay his friend exactly X rupees.
->  What is the minimum number of coins Chef needs to pay exactly X rupees?

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single line of input containing a single integer X.

Output Format
-------------
For each test case, output on a new line the minimum number of coins Chef needs to pay exactly X rupees.

Sample:- 

input               output
4
53                    3
100                   0
9                     9
11                    1
'''

# Answer 

N = int(input())
for i in range(N):
    X = int(input())
    print(X % 10)
    