'''
-> The Chessboard Distance for any two points (X1,Y1)(X1,Y1) and (X2,Y2)(X2,Y 2) on a Cartesian plane is defined as 
max(∣X1−X2∣,∣Y1−Y2∣)max(∣X1−X2∣,∣Y 1−Y 2∣).

-> You are given two points (X1,Y1)(X1,Y1) and (X2,Y2)(X2,Y2). Output their Chessboard Distance.

Note that, ∣P∣∣P∣ denotes the absolute value of integer P. For example, 
∣−4∣=4∣−4∣=4 and ∣7∣=7∣7∣=7.

Input Format
--------------
-> First line will contain T, the number of test cases. Then the test cases follow.
-> Each test case consists of a single line of input containing 4 space separated integers - X1,Y1,X2,Y2X1,Y1,X2,Y 2​- as defined in the problem statement.

Output Format
---------------
For each test case, output in a single line the chessboard distance between (X1,Y1)(X1,Y1) and (X2,Y2)(X2,Y2​)

sample:- 

input                   output 
3
2 4 5 1                    3
5 5 5 3                    2
1 4 3 3                    2


'''

# Answer
n = int(input())
for i in range(n):
    a , b , c , d= map(int, input().split())
    res = abs(a - c)
    res1 = abs(b - d)
    print(max(res, res1))