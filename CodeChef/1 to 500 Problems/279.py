'''
Audible Range
---------------
-> Chef's dog binary hears frequencies starting from 67 Hertz to 45000 Hertz (both inclusive).
-> If Chef's commands have a frequency of X Hertz, find whether binary can hear them or not.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single integer X - the frequency of Chef's commands in Hertz.

Output Format
--------------
-> For each test case, output on a new line YES, if binary can hear Chef's commands. Otherwise, print NO.
-> The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

sample:-

input               output

5
42                    NO
67                    YES
402                   YES
45000                 YES
45005                 NO


'''

# Answer
n = int(input())
for i in range(n):
    A = int(input())
    if A < 67 or A > 45000:
        print("NO")
    else:
        print("YES")