'''
The Cooler Dilemma 2
---------------------
-> The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool.
-> He has two options available:
-> Rent a cooler at the cost of X coins per month.Purchase a cooler for Y coins.
-> Chef wonders what is the maximum number of months for which he can rent the cooler such that
->  the cost of renting is strictly less than the cost of purchasing it.

Input Format
--------------
-> The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
-> The first and only line of each test case contains two integers X and Y, as described in the problem statement.

Output Format
-------------
-> For each test case, output the maximum number of months for which he can rent the cooler such that the cost of renting is strictly less than the cost of purchasing it.
-> If Chef should not rent a cooler at all, output 0.

Sample Input
-------------------

input               output
45
5 12                  2
5 5                   0
2 5                   2
2 1                   0   
5 10                  1  
'''

# Answer

def Solve():
    X, Y = map(int, input().split())
    months = (Y - 1) // X 
    print(months)

N = int(input())
for i in range(N):
    Solve()