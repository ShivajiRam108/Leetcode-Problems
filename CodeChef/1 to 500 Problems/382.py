'''
Six Friends
---------------
-> Six friends go on a trip and are looking for accommodation.
-> After looking for hours, they find a hotel which offers two types of rooms — double rooms and triple rooms.
-> A double room costs Rs. X, while a triple room costs Rs. Y.
-> The friends can either get three double rooms or get two triple rooms.
->  Find the minimum amount they will have to pay to accommodate all six of them.

Input Format
------------
-> The first line contains a single integer T - the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains two integers X and Y - the cost of a double room and the cost of a triple room.

Output Format
--------------
-> For each testcase, output the minimum amount required to accommodate all the six friends.

Sample:- 

input                   output
3
10 15                    30
6 8                      18
4 8                      12
'''

# Answer 
N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    x1 = X * 3 
    x2 = Y * 2 
    print(min(x1, x2))