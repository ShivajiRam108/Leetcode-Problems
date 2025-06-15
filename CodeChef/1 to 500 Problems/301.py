'''
Right There
--------------
-> If you wanna party, if you, if you wanna partyThen put your hands up Chef wants to host a party with a total of N people.
-> However, the party hall has a capacity of X people. Find whether Chef can host the party.

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers N and X — the total number of people and the capacity of the party hall.

Output Format
---------------
-> For each test case, output on a new line, YES, if Chef can host the party and NO otherwise.
-> Each character of the output may be printed in either uppercase or lowercase.
-> That is, the strings NO, no, nO, and No will be treated as equivalent.

Sample :-

input                 output 

4
2 5                     YES
4 3                     NO
6 6                     YES
10 9                    NO
'''

#Answer
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    if A <= B:
        print("YES")
    else:
        print("NO")

# Time Complexity: O(T)
# Space Complexity: O(1)'

# another way
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print("YES" if A <= B else "NO")