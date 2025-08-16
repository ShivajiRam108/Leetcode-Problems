'''
Find Remainder
---------------
-> Write a program to find the remainder when an integer A is divided by an integer B.

Input
------
-> The first line contains an integer T, the total number of test cases. Then T lines follow, each line contains two Integers A and B.

Output
-------
-> For each test case, find the remainder when A is divided by B, and display it in a new line.

Sample:- 

input               output
3 
1 2                   1
100 200               100
40 15                 10
'''

# Answer

N = int(input())
for i in range(N):
    X , Y = map(int, input().split())
    print(X % Y)