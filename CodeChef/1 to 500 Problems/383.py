'''
Chef and Wire Frames
---------------------
-> Chef has a rectangular plate of length Ncm and width Mcm. He wants to make a wireframe around the plate. 
-> The wireframe costs X rupees per cm.Determine the cost Chef needs to incur to buy the wireframe.

Input Format
--------------
-> First line will contain T, the number of test cases. Then the test cases follow.
-> Each test case consists of a single line of input, containing three space-separated
-> integers N,M, and X — the length of the plate, width of the plate, and the cost of frame per cm.

Output Format
--------------
-> For each test case, output in a single line, the price Chef needs to pay for the wireframe.

Sample :- 

input               output
3
10 10 10             400
23 3 12              624
1000 1000 1000       4000000

'''

# Answer 

N = int(input())
for i in range(N):
    X , Y , Z = map(int, input().split())
    x1 = X * 2 
    x2 = Y * 2 
    res = x1 + x2 
    print(res * Z)
