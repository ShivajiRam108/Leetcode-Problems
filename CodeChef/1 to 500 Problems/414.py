'''
Profit Increment
-----------------
-> Chef recently started selling a special fruit.He has been selling the fruit for X rupees (X is a multiple of 100).
->  He earns a profit of Y rupees on selling the fruit currently.Chef decided to increase the selling price by 10%. 
-> Please help him calculate his new profit after the increase in selling price.
=> Note that only the selling price has been increased and the buying price is same.

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single line of input containing two space-separated 
-> integers X and Y denoting the initial selling price and the profit respectively.

Output Format
---------------
-> For each test case, output a single integer, denoting the new profit.

Sample :- 

input               output
4  
100 10                20
200 5                 25
500 10                60
100 7                 17
'''

# Answer

N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    res1 = X - Y 
    res2 = X + ( X * 0.1)
    res3 = res2 - res1
    print(int(res3))  