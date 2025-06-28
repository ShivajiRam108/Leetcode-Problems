'''
Minimum number of Flips
------------------------
-> Chef has an array A of length N consisting of 1 and −1 only.
-> In one operation, Chef can choose any index (1≤i≤N) and multiply the element A i  by −1.
-> Find the minimum number of operations required to make the sum of the array equal to 0. 
-> Output -1 if the sum of the array cannot be made 0.

Input Format
--------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> First line of each test case consists of a single integer N denoting the length of the array.
-> Second line of each test case contains N space-separated integers A1 ,A2 , …, A N  denoting the array A.

Output Format
--------------
-> For each test case, output the minimum number of operations to make the sum of the array equal to 0.
->  Output -1 if it is not possible to make the sum equal to 0.

Sample 

input                       output 

4
4
1 1 1 1                        2
5
1 -1 1 -1 1                   -1
6
1 -1 -1 1 1 1                  1
2
1 -1                           0
'''

# Answer 
N = int(input())
for i in range(N):
    A = int(input())
    X = list(map(int, input().split()))
    count1 = X.count(1)
    count_1 = X.count(-1)
    deff = abs(count1 - count_1)
    if deff % 2 != 0:
        print(-1)
    else:
        print(deff // 2)