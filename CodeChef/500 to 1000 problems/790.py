'''
The Lead Game
--------------
-> The game of billiards involves two players knocking 3 balls around on a green baize table.
->  Well, there is more to it, but for our purposes this is sufficient.
-> The game consists of several rounds and in each round both players obtain a score, based on how well they played.
-> Once all the rounds have been played, the total score of each player is determined by adding up the scores in all the rounds 
-> and the player with the higher total score is declared the winner.
-> The Siruseri Sports Club organises an annual billiards game where the top two players of Siruseri play against each other.
->  The Manager of Siruseri Sports Club decided to add his own twist to the game by changing the rules for determining the winner.
-> In his version, at the end of each round, the cumulative score for each player is calculated, and the leader and her current lead are found.
-> Once all the rounds are over the player who had the maximum lead at the end of any round in the game is declared the winner.
-> The winner of this game is Player 1 as he had the maximum lead (58 at the end of round 1) during the game.
-> Your task is to help the Manager find the winner and the winning lead.
-> You may assume that the scores will be such that there will always be a single winner. That is, there are no ties.

Input
---------
-> The first line of the input will contain a single integer N (N ≤ 10000) indicating the number of rounds in the game.
->  Lines 2,3,...,N+1 describe the scores of the two players in the N rounds. Line i+1 contains two integer Si and Ti,
-> the scores of the Player 1 and 2 respectively, in round i. You may assume that 1 ≤ Si ≤ 1000 and 1 ≤ Ti ≤ 1000.

Output
--------
-> Your output must consist of a single line containing two integers W and L, where W is 1 or 2 and indicates the winner and L is the maximum lead attained by the winner.

Sample:- 

input                       output 
5
140 82                        1 58
89 134
90 110
112 106
88 90
'''

# Answer 
N = int(input())
res = []
for i in range(N):
    a, b = map(int,input().split())
    if a > b:
        res.append(a-b)
    else:
        res.append(b-a)
print(min(res),max(res))

#  (Or)

N = int(input())
p1_total = 0
p2_total = 0
winner = 0
max_score = 0
for i in range(N):
    X, Y = map(int,input().split())
    p1_total += X 
    p2_total += Y 
    lead = p1_total - p2_total 
    Z = abs(lead)
    if Z > max_score:
        max_score = Z 
        if lead > 0:
            winner = 1
        else:
            winner = 2
print(winner , max_score)

