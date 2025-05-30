'''
#  Q :- Small factorials
---------------------------------
=> You are asked to calculate factorials of some small positive integers.

Input
--------
-> An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100

Output
--------
-> For each integer n given at input, display a line with the value of n!

** => Note: For larger numbers, their factorial can overflows any available numeric data type in C.

Sample 1:
Input :                        output :

4
1                               1
2                               2
5                               120
3                               6

'''

#  Answer 
n = int(input())
for i in range(n):
    a = int(input())
    fac = 1
    for j in range(1,a + 1):
        fac *=  j
    print(fac)