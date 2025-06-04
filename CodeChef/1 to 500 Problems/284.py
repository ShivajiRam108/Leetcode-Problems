'''
Best of Two
-----------
-> Chef took an examination two times. In the first attempt, he scored X marks while in the second attempt he scored Y marks.
-> According to the rules of the examination, the best score out of the two attempts will be considered as the final score.
-> Determine the final score of the Chef.

Input Format
--------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first line of each test case contains two integers X and Y — the marks scored by Chef in the first attempt and second attempt respectively.

Output Format
-------------
-> For each test case, output the final score of Chef in the examination.

Sample:-

input               output 
4
40 60               60
67 55               67
50 50               50
1 100               100
'''
# Answer
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    if A > B:
        print(A)
    else:
        print(B)