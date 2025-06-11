'''
Cyclic Quadrilateral
----------------------
-> Read problem statements in Mandarin Chinese, Russian, and Vietnamese as well.
-> You are given the sizes of angles of a simple quadrilateral (in degrees) A, B, C and D,
-> in some order along its perimeter. Determine whether the quadrilateral is cyclic.

=> Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 180 ∘ .

Input
--------
-> The first line of the input contains a single integer T denoting the number of test cases.
-> The description of T test cases follows.
-> The first and only line of each test case contains four space-separated integers A, B, C and D.

Output
-------
-> Print a single line containing the string "YES" if the given quadrilateral is cyclic or "NO" if it is not (without quotes).
-> You may print each character of the string in uppercase or lowercase
-> (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Sample

input                    output

3 
10 20 30 300             NO
10 20 170 160            YES
179 1 179 1              NO
'''

#Answer
N = int(input())
for i in range(N):
    A , B , C, D = map(int, input().split())
    if (A + C == 180) or (B + D == 180):
        print("YES")
    else:
        print("NO")