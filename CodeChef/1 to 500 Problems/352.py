'''
Chef and Chapters
-----------------
-> This semester, Chef took X courses. Each course has Y units and each unit has Z chapters in it.
-> Find the total number of chapters Chef has to study this semester.

Input Format
--------------
-> The first line will contain T, the number of test cases. Then the test cases follow.
-> Each test case consists of a single line of input, containing three space-separated integers X,Y, and Z.

Output Format
--------------
-> For each test case, output in a single line the total number of chapters Chef has to study this semester.

Sample :- 

input                 output 
3
1 1 1                    1
2 1 2                    4
1 2 3                    6
'''

N = int(input())
for i in range(N):
    X, Y , Z = map(int,input().split())
    print(X * Y * Z)