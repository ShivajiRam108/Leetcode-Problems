'''
Instagram
-----------
-> Chef categorises an instagram account as spam, if, the following count of the account is more than 10 times the count of followers.
-> Given the following and follower count of an account as X and Y respectively, find whether it is a spam account.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers X and Y — the following and follower count of an account, respectively.

Output Format
--------------
-> For each test case, output on a new line, YES, if the account is spam and NO otherwise.
-> You may print each character of the string in uppercase or lowercase. 
-> For example, the strings YES, yes, Yes and yES are identical.


Sample :- 

input           output
4
1 10             NO
10 1             NO
11 1             YES
97 7             YES
'''

# Answer 

N = int(input())
for i in range(N):
    X , Y = map(int, input().split())
    if X > 10 * Y:
        print("YES")
    else:
        print("NO")