'''
IPL Ticket Rush
-----------------
-> DAIICT college students want to attend an IPL match.A total of N students from the college want to go while only M tickets are available for the match.
-> Determine how many students won't be able to book tickets.

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers N and M — the number of students
->  wants to go and the total number of tickets available, respectively.

Output Format
--------------
-> For each test case, output on a new line the number of students who won't be able to book tickets.

sample:-

input           output 

4
5 3                 2
5 7                 0
4 1                 3
8 8                 0
'''

# Answer:-
n = int(input())
for i in range(n):
    a , b = map(int, input().split())
    if a <= b:
        print(0)
    else:
        print(a - b)