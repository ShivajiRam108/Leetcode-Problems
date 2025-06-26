'''
Get Lowest Free
----------------
-> Chef goes to the supermarket to buy some items. Luckily there's a sale going on under which Chef gets the following offer:
-> If Chef buys 3 items then he gets the item (out of those 3 items) having the lowest price as free.
=> For e.g. if Chef bought 3 items with the cost 6, 2 and 4, then he would get the item with cost 2 as free.
-> So he would only have to pay the cost of the other two items which will be 6+4=10.
-> Chef buys 3 items having prices A, B and C respectively. What is the amount of money Chef needs to pay?

Input Format
--------------
-> The first line will contain an integer T - number of test cases. Then the test cases follow.
-> The first and only line of each test case contains three integers A,B,C - the prices of the items bought by Chef.

Output Format
--------------
-> For each test case, output the price paid by Chef.

Sample

input                   output

3
6 2 4                     10
3 3 3                     6
8 4 4                     12
'''
# Answer

N = int(input())
for i in range(N):
    X , Y , Z = map(int, input().split())
    min1 = min( X, Y, Z)
    print((X + Y + Z )- min1)