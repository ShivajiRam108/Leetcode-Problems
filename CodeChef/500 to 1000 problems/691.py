'''
Valentine is Coming
--------------------
-> Valentine's Day is approaching and thus Chef wants to buy some chocolates for someone special.
-> Chef has a total of X rupees and one chocolate costs Y rupees.
-> What is the maximum number of chocolates Chef can buy?

Input Format
--------------
=> First line will contain T, the number of test cases. Then the test cases follow.
-> Each test case contains a single line of input, two integers ,Y
-> X,Y - the amount Chef has and the cost of one chocolate respectively.

Output Format
--------------
-> For each test case, output the maximum number of chocolates Chef can buy.

sample:-

input               output

4
5 10                0
16 5                3
35 7                5
100 1               100
'''
# Answer:-
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a // b)