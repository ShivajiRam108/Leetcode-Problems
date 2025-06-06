'''
Decrement OR Increment
-----------------------
-> Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 
-> otherwise decrement its value by 1.

Input Format
----------------
-> First line will contain a number N.

Output Format
-------------
-> Output a single line, the new value of the number.

Sample:-

input               output

5                     4
8                     9
'''

#Answer

N = int(input())
if N % 4 == 0:
    N += 1
else:
    N -= 1
print(N)
