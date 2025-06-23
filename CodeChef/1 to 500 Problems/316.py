'''
Messi vs Ronaldo
----------------
-> In Chefland, a football player gets 2 points for each goal and 1 point for each assist.
-> Messi has A goals and B assists this season, whereas Ronaldo has X goals and Y assists.
-> Find out the player with more points this season.

Input Format
--------------
-> The first and only line of input will contains four space-separated integers A, B, X and Y, the number of goals 
-> and assists that Messi has and the number of goals and assists that Ronaldo has, respectively.

Output Format
--------------
-> Print a single line containing:
-> Messi, if Messi has more points than Ronaldo.
-> Ronaldo, if Ronaldo has more points than Messi.
-> Equal, if both have equal points.
-> You can print each character in uppercase or lowercase. For example, the strings Messi, MESSI, messi, and MeSSi are considered identical.

Sample :-

input                   output 

40 30 50 10               Equal
91 22 60 30               Messi
60 30 80 20               Ronaldo
'''

# Answer
A , B , C , D = map(int, input().split())
X = A * 2
Y = C * 2 

if X + B == Y + D:
    print("Equal")
elif X + B > Y + D:
    print("Messi")
else:
    print("Ronaldo")