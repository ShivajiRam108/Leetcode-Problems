'''
Read Pages
-----------
-> Chef has started studying for the upcoming test. The textbook has N pages in total.
-> Chef wants to read at most X pages a day for Y days.
-> Find out whether it is possible for Chef to complete the whole book.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of each test case contains three space-separated integers N,X, and Y — the number of pages,
-> the number of pages Chef can read in a day, and the number of days.

Output Format
--------------
-> For each test case, output on a new line, YES, if Chef can complete the whole book in given time, and NO otherwise.
-> You may print each character of the string in uppercase or lowercase.
-> For example, Yes, YES, yes, and yES are all considered identical.


Sample :- 

input                   output 
4
5 2 3                    Yes
10 3 3                   No
7 7 1                    Yes
3 2 1                    No

'''

# Answer 

N = int(input())
for i in range(N):
    X , Y , Z = map(int, input().split())
    if X <= Y * Z:
        print("YES")
    else:
        print("NO")