'''
Parliament
-------------
-> An important resolution is being discussed in the Parliament of Chefland.
-> There are N members present in the Parliament out of which X members voted in favour of the resolution and the remaining voted against it.
-> According to the constitution of Chefland, a resolution is passed if and only if half or more than half the 
-> members present in the Parliament vote in favour of the resolution.Determine if the resolution is passed or not.

Input Format
--------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains two space-separated integers N and X — the total number of members
->  present in the Parliament and the number of members who voted in favour of the resolution.

Output Format
--------------
-> For each test case, output YES if the resolution is passed. Otherwise, output NO.
-> You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs and Yes will be considered identical).

Sample:

input                    output
4
12 6                      YES
9 4                       NO
9 5                       YES
12 0                      NO
'''

# Answer

N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    if 2 * Y >= X:
        print("YES")
    else:
        print("NO")

# (Or)
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    if Y >= X / 2:
        print("YES")
    else:
        print("NO")