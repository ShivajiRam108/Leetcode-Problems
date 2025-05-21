'''
The Last Levels
---------------------
-> Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.
-> There are X levels remaining in the game, and each level takes Chef Y minutes to complete. 
-> To protect against eye strain, Chef also decides that every time he completes 3 levels, he will take a Z minute break from playing.
-> Note that there is no need to take this break if the game has been completed.

-> How much time (in minutes) will it take Chef to complete the game?

Input Format
---------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of input will contain three space-separated integers X, Y, and Z.

Output Format
--------------
-> For each test case, output on a new line the answer — the length of Chef's gaming session.

sample:-

input                   output 

4
2 12 10                     24
3 12 10                     36
7 20 8                      156
24 45 15                    1185
'''
#Answer:- 
n = int(input())
for i in range(n):
    a , b , c = map(int, input().split())
    res = 0
    if a % 3 == 0:
        res = (a// 3) - 1
    else:
        res = (a // 3)
    print(a * b + res * c)