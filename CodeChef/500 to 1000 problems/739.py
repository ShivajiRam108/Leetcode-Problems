'''
Chef Fantasy 11
---------------
-> All of Chef's friends are playing fantasy cricket based upon the ODI World Cup, and Chef would like to join them.
-> For a certain cricket match, Chef has decided upon his team of 11 players.
-> However, he hasn't yet decided who should be the captain and who should be the vice-captain.
-> He's narrowed his decision down to N players out of the 11, from which he'll choose one to be the captain and one to be the vice captain.
-> How many different choices does he have?

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and the only line of each testcase contains a single integer N, the number of players Chef is considering.

Output Format
-------------
-> For each test case, output on a new line the number of possible choices of captain and vice-captain.

Sample :-

input                 output
2
2                      2
3                      6
'''
# Answer
N = int(input())
for i in range(N):
    X = int(input())
    print(X * (X - 1))

# (Or)
N = int(input())
for i in range(N):
    A = int(input())
    if A < 2:
        print(0)
    else:
        print(A * (A - 1))