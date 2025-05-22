'''
Blackjack
-----------
-> Chef is playing a variant of Blackjack, where 3 numbers are drawn and each number lies between 1 and 10 (with both 1 and 10 inclusive).
-> Chef wins the game when the sum of these 3 numbers is exactly 21.

=> Given the first two numbers A and B, that have been drawn by Chef, what should be 3-rd number that should be drawn by the Chef in order to win the game?

=> Note that it is possible that Chef cannot win the game, no matter what is the 3-rd number. In such cases, report 1−1 as the answer.

Input Format
-------------
-> The first line will contain an integer T - number of test cases. Then the test cases follow.
-> The first and only line of each test case contains two integers A and B - the first and second number drawn by the Chef.

Output Format
--------------
-> For each testcase, output the 3-rd number that should be drawn by the Chef in order to win the game. Output1−1 if it is not possible for the Chef to win the game.

sample:-

input               output
3
1 10                    10
1 5                     -1
4 9                     8
'''

# Answer:-
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = 21 - (a + b)
    if 1 <= c <= 10:
        print(c)
    else:
        print(-1)