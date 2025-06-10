'''
Pass or Fail
----------------
-> Chef is struggling to pass a certain college course.
-> The test has a total of N questions, each question carries 3 marks for a correct answer and −1 for an incorrect answer.
-> Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got X questions correct and the rest of them incorrect.
->  For Chef to pass the course he must score at least P marks.

=> Will Chef be able to pass the exam or not?

Input Format
------------
-> First line will contain T, number of testcases. Then the testcases follow.
-> Each testcase contains of a single line of input, three integers N,X,P.

Output Format
--------------
-> For each test case output "PASS" if Chef passes the exam and "FAIL" if Chef fails the exam.
-> You may print each character of the string in uppercase or lowercase 
-> (for example, the strings "pASs", "pass", "Pass" and "PASS" will all be treated as identical).

Sample 

input                output
3
5 2 3                 PASS
5 2 4                 FAIL
4 0 0                 FAIL
'''
# Answer
N = int(input())
for i in range(N):
    N , X , P = map(int,input().split())
    A = (N - X) -1
    B = X * 3 
    C = A + B 
    if C >= P:
        print("PASS")
    else:
        print("FAIL")

#  another approach
N = int(input())
for i in range(N):
    N, X, P = map(int, input().split())
    score = X * 3 - (N - X)
    if score >= P:
        print("PASS")
    else:
        print("FAIL")