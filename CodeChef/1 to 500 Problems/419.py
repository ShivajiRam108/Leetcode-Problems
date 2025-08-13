'''
Fill the Bucket
-----------------
-> Chef has a bucket having a capacity of K liters. It is already filled with X liters of water.
-> Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.

Input Format
-------------
-> The first line will contain T- the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains two space separated integers K and X - as mentioned in the problem.

Output Format
--------------
-> For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.

Sample :- 

input               output
2 
5 4                   1
15 6                  9
'''

# Answer:- 

N = int(input())
for i in range(N):
    X , Y = map(int, input().split())
    if X > Y:
        print(X - Y)
    else:
        print(Y - X)