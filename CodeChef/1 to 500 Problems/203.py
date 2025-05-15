'''
Cricket World Cup Qualifier
The cricket World Cup has started in Chefland. There are many teams participating in the group stage matches. Any team that scores 
12
12 or more points in the group stage matches qualifies for the next stage.

You know the score that a particular team has scored in the group stage matches. Determine if the team has qualified for the next stage or not.

Input Format
-----------------
The first and only line of input consists of an integer 
X
X denoting the total points scored by the given team in the group stage matches.

Output Format
------------------
Output Yes, if the team has qualified for the next stage, and No otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).


Sample 1:
Input : 3 
Output : No
 
Sample 2:
input :  17 
output :  YES
'''

#  Answer code 
n = int(input())
if n >= 12:
    print("YES")
else:
    print("NO")