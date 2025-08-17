'''
Ezio and Guards
-----------------
-> Ezio can manipulate at most X number of guards with the apple of eden.
-> Given that there are Y number of guards, predict if he can safely manipulate all of them.

Input Format
--------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> Each test case contains of a single line of input, two integers X and Y.

Output Format
--------------
-> For each test case, print YES if it is possible for Ezio to manipulate all the guards. Otherwise, print NO.
-> You may print each character of the string in uppercase or lowercase 
-> (for example, the strings YeS, yEs, yes and YES will all be treated as identical).

Sample :- 

input                output 
3
5 7                    NO
6 6                    YES
9 1                    YES
'''
# Answer:- 

N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    if X >= Y:
        print("YES")
    else:
        print("NO")