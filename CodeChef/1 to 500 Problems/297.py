'''
Counting Words
----------------
-> Harsh was recently gifted a book consisting of N pages.
-> Each page contains exactly M words printed on it. As he was bored, he decided to count the number of words in the book.
-> Help Harsh find the total number of words in the book.

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers on a single line,
-> N and M — the number of pages and the number of words on each page, respectively.

Output Format
-------------
-> For each test case, output on a new line, the total number of words in the book.

Sample 

input                output

4
1 1                    1
4 2                    8
2 4                    8
95 42                  3990
'''
#Answer
N = int(input())
for i in range(N):
    A, B = map(int,input().split())
    print(A * B)
  