'''
Discount
---------
-> Alice buys a toy with a selling price of 100 rupees. There is a discount of x percent on the toy. 
-> Find the amount Alice needs to pay for it.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of each test case contains a single integer, x — the discount on the toy.

Output Format
--------------
-> For each test case, output on a new line the price that Alice needs to pay.

Sample :- 

input                output
4
5                      95
9                      91
11                     89
21                     79
'''

# Answer 

N = int(input())
for i in range(N):
    X = int(input())
    print(100 - X)