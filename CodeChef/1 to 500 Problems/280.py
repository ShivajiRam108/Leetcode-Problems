'''
Bone Appetit
-------------
-> Trick or treat, bags of sweets, ghosts are walking down the streetIt's Halloween and Suri Bhai is out to get his treats.
-> There are two sectors in his neighborhood, "Bones" and "Blood". They have N and M people, respectively.
-> Each person in "Bones" will hand out X treats, and each person in "Blood" will hand out Y treats.
-> How many treats does Suri Bhai get from visiting everyone in his neighborhood in total?

Input Format
-------------
-> The first line of input contains two space-separated integers N and M — the number of people in "Bones" and "Blood", respectively.
-> The second line of input contains two space-separated integers X and Y — the number of treats handed out by each person in "Bones" and "Blood", respectively.

Output Format
--------------
-> For each test case output a single integer: the total number of treats Suri Bhai will receive.

Sample:-

input                   output

4 2
5 6                       32
'''

# Answer
A , B = map(int,input().split())
C , D = map(int, input().split())
X = A * C 
Z = B * D 
print(X + Z)