'''
Battery Health
----------------
-> Apple considers any iPhone with a battery health of 80% or above, to be in optimal condition.
-> Given that your iPhone has X% battery health, find whether it is in optimal condition.

Input Format
-------------
->The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of each test case contains an integer X — the battery health.

Output Format
------------
-> For each test case, output on a new line, YES, if the battery is in optimal condition, and NO otherwise.
-> You may print each character in uppercase or lowercase. For example, NO, no, No and nO, are all considered identical.

Sample:-

input                   output

4
97                      YES
42                      NO
80                      YES
10                      NO
'''
# Answer
N = int(input())
for i in range(N):
    A = int(input())
    if A >= 80:
        print("YES")
    else:
        print("NO")

# another way
N = int(input())
for i in range(N):
    A = int(input())
    print("YES" if A >= 80 else "NO")