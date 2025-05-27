'''
Kitchen Timings
----------------
-> The working hours of Chef’s kitchen are from X pm to Y pm (1≤X<Y≤12)(1≤X<Y≤12).

-> Find the number of hours Chef works.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers X and Y — the starting and ending time of working hours respectively.

Output Format
-------------
-> For each test case, output on a new line, the number of hours Chef works.

sample:-
input                   output 

4
1 2                     1
3 7                     4
9 11                    2
2 10                    8 
'''

# Answer
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print(b - a)