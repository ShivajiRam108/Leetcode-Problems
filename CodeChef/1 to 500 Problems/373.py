'''
Interior Design
----------------
-> Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.
-> For the first style, tiling the floor will cost X1  rupees and painting the walls will cost Y1 rupees.
-> For the second style, tiling the floor will cost X2 rupees and painting the walls will cost Y2 rupees.
-> Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior design?

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single line of input, containing 4 space-separated integers 
-> X1 ,Y1 ,X2,2 as described in the statement.

Output Format
--------------
-> For each test case, output on a new line the amount Chef will pay for interior design.

Sample :- 

input                   output 
4
10 20 9 25                 30
10 20 9 20                 29
10 20 20 10                30
100 43 85 61               143
'''

# Answer

N = int(input())
for i in range(N):
    X, Y, Z, R = map(int, input().split())
    A = X + Y 
    B = Z + R 
    S = min(A, B)
    print(S)