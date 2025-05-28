'''
Weights
--------
-> Chef is playing with weights. He has an object weighing W units.
-> He also has three weights each of X ,Y  and Z units respectively.
-> Help him determine whether he can measure the exact weight of the object with one or more of these weights.
-> If it is possible to measure the weight of object with one or more of these weights, print YES, otherwise print NO.

Input Format
---------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of single line containing a four positive integers W, X, Y, and Z.

Output Format
---------------
-> For each test case, output on a new line YES if it is possible to measure the weight of object with one or more of these weights,
-> otherwise print NO.You may print each character of the string in either uppercase or lowercase
-> (for example, the strings yes, YES, Yes, and yeS will all be treated as identical).

sample:-

input               output

4
5 2 1 6                NO
7 9 7 2                YES
20 8 10 12             YES
20 10 11 12            NO
'''

n = int(input())
for i in range(n):
    A, B , C , D = map(int, input().split())
    res = {B , C , D , B + C , B + D , C + D , B + C + D}
    if A in res:
        print("YES")
    else:
        print("NO")

