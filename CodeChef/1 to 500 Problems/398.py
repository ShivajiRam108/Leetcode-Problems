'''
True and False Paper
----------------------
-> Alice wrote an exam containing N true or false questions (i.e. questions whose answer is either true or false).
->  Each question is worth 1 mark and there is no negative marking in the examination. Alice scored K marks out of N.
-> Bob wrote the same exam but he marked each and every question as the opposite of what Alice did, i.e, 
-> for whichever questions Alice marked true, Bob marked false and for whichever questions Alice marked false, Bob marked true.
-> Determine the score of Bob.

Input Format
--------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains two space-separated integers N and K — the total 
-> number of questions in the exam and the score of Alice.

Output Format
--------------
-> For each test case, output on a new line the score of Bob.

Sample :- 

input           output
3
1 1                0
50 0               50
100 76             24
'''

# Answer

N = int(input())
for i in range(N):
    X ,  Y = map(int, input().split())
    print(X - Y)