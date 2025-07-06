'''
Couple Game
----------------
-> There are G girl and B boy students at IIT (BHU) such that B>G.
-> If ICM were a team game where teams could only be of size 2, having exactly 1 girl student and 1 boy student,
-> what would be the minimum number of boy students from IIT (BHU) who would not be able to participate?

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of each test case contains two space-separated integers G and B,
-> the number of girl and boy students at IIT (BHU) respectively.

Output Format
---------------
-> For each test case, output a single integer on a new line, the minimum number of boy students from IIT
-> (BHU) who would not be able to participate.

Sample :- 

input                   output 
3
1 3                        2
2 4                        2
3 10                       7
'''

# Answer 

N = int(input())
for i in range(N):
    X , Y = map(int, input().split())
    print(Y - X)
