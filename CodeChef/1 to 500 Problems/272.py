'''
Donation Drive
----------------
-> A blood drive aims to collect N number of blood donations.
-> The drive has collected X donations so far. 
-> Find the remaining number of donations needed to reach the target.

Input Format
-----------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case contains two space-separated integers N and X
-> X — the number of required donations and the number of collected donations, respectively.

Output Format
------------
-> For each test case, output on a new line, the remaining number of donations needed to reach the target.

sample:- 

input                       output 

4
5 2                            3
3 3                            0
5 4                            1
7 5                            2 
'''

# Answer 

n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print(a - b)