'''
Dracula Eats
-------------
Eat, drink, and be scary

-> There are N spooky days left until Halloween.
-> Dracula dines at a mysterious restaurant that changes its spooky menu daily. He particularly enjoys what they serve on Tuesday.
-> Today is Monday, so he wishes to calculate how many times he can indulge in his favourite menu in the next N days (including today) before Halloween.

=> Note that Dracula follows the standard 7-day calendar, with Tuesday immediately following Monday.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> usThe only line of each test case contains a single integer N, denoting the number of spooky days.

Output Format
-------------
For each test case, output on a new line the number of times Dracula would have had his favorite meal after N days.

Sample :-

input               output 

4
1                     0
10                    2
15                    2
16                    3
'''

# Answer
N = int(input())
for i in range(N):
    X = int(input())
    S = 0
    A = X // 7
    S += A
    C = X % 7 
    if (C >= 2):
        S += 1
    print(S)

# Another way 
N = int(input())
for i in range(N):
    X = int(input())
    if X <= 7:
        print(0)
    else:
        print((X // 8 )+1)
