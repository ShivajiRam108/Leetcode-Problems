'''
Small Factorial
----------------
=> Write a program to find the factorial value of any number entered by the user.

Input Format
------------
=> The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.

Output Format
---------------
=> For each test case, display the factorial of the given number N in a new line.

Sample :-

input               output 
3 
3                     6
4                     24
5                     120
'''

# Answer
N = int(input())
for i in range(N):
    X = int(input())
    res = 1
    for i in range(1, X + 1):
        res *= i
    print(res)

