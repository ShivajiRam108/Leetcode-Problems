'''
Roller Coaster
--------------
-> Chef's son wants to go on a roller coaster ride. The height of Chef's son is X inches while the minimum height
-> required to go on the ride is H inches. Determine whether he can go on the ride or not.

Input Format
-------------
-> The first line contains a single integer T - the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains two integers X and H - the height 
-> of Chef's son and the minimum height required for the ride respectively.

Output Format
-----------
-> For each test case, output in a single line, YES if Chef's son can go on the ride. Otherwise, output NO.
-> You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical)

Sample:-

input               output

4
15 20               NO
50 48               YES
32 32               YES
38 39               NO

'''
# Answer
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    if  A >= B:
        print("YES")
    else:
        print("NO")
