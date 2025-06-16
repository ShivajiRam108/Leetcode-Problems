'''
Second Max of Three Numbers
---------------------------
=> Problem Statement
=> Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

Input
-------
-> First line contains the number of triples, N.
-> The next N lines which follow each have three space separated integers.

Output
------
-> For each of the N triples, output one new line which contains the second-maximum integer among the three.

Sample:-

input               output

3
1 2 3                 2
10 15 5               10
100 999 500           500
''' 

# Answer

N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    if A > B:
        if A > C:
            if B > C:
                print(B)
            else:
                print(C)
        else:
            print(A)
    else:
        if B > C:
            if A > C:
                print(A)
            else:
                print(C)
        else:
            print(B)