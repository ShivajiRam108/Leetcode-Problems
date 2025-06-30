'''
Best of Two
-----------
-> Alice and Bob are playing a game. Each player rolls a standard six-sided die three times. 
-> The score of a player is calculated as the sum of the two highest rolls. The player with the higher score wins. 
-> If both players have the same score, the game ends in a tie.Determine the winner of the game or if it is a tie.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case contains six space-separated integers A1 A2 A3, B1, B2 abd B3  — the values Alice gets in her 3 dice rolls, 
-> followed by the values which Bob gets in his 3 dice rolls.

Output Format
------------
-> For each test case, output on a new line Alice if Alice wins, Bob if Bob wins and Tie in case of a tie.
-> Note that you may print each character in uppercase or lowercase.
-> For example, the strings tie, TIE, Tie, and tIe are considered identical.

Sample:- 

input                   output

3
3 2 5 6 1 1             Alice
4 4 5 6 4 1             Bob
6 6 6 6 6 1             Tie
'''

# Answer

N = int(input())
for i in range(N):
    A, B, C, D, E, F = map(int, input().split())
    X = [A, B, C]
    Y = [D, E, F]

    alice_total = sum(X) - min(X)
    bob_total = sum(Y) - min(Y)

    if alice_total == bob_total:    
        print("Tie")
    elif alice_total  > bob_total:
        print("Alice")
    else:
        print("Bob")