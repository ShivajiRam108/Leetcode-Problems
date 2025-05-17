'''
Chess Ratings
-----------------
-> Alice has recently started playing Chess. Her current rating is X. She noticed that when she wins a game, her rating increases by 8 points.
-> Can you help Alice in finding out the minimum number of games she needs to win in order to make her rating greater than or equal to Y?

Input Format
----------------
-> The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
-> The first line of each test case contains two integers X and Y, as described in the problem statement.

Output Format
---------------
-> For each test case, output the minimum number of games that Alice needs to win in order to make her rating greater than or equal to Y.

sample :-

input                   output 

4
10 10                       0
10 17                       1
10 18                       1
10 19                       2


'''

# Answer 

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a >= b:
        print(0)
    else:
        print((b-a+7 )//8)