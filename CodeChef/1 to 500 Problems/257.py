'''
Biryani classes
--------------------
-> According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef.
-> Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is Y coins.
-> What is the total amount of money that Chef will have to pay?

Input Format
----------------
-> The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
-> The first and only line of each test case contains two space-separated integers X and Y, as described in the problem statement.

Output Format
----------------
-> For each test case, output on a new line the total amount of money that Chef will have to pay.

smaple:- 

input               output 
4
1 10                10
1 15                15 
2 10                20
2 15                30
'''

# Answer:-
n= int(input())
for i in range(n):
    a , b = map(int, input().split())
    print(a * b)