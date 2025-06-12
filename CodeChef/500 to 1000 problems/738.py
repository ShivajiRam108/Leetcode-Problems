'''
Too many items
---------------
-> Chef bought N items from a shop.
-> Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.
-> 1 polybag can contain at most 10 items. What is the minimum number of polybags needed by Chef?

Input Format
------------
-> The first line will contain an integer T - number of test cases. Then the test cases follow.
-> The first and only line of each test case contains an integer N - the number of items bought by Chef.

Output Format
------------
-> For each test case, output the minimum number of polybags required.

Sample:-

input                     output 

3
20                        2
24                        3
99                        10
'''
N = int(input())
for i in range(N):
    X = int(input())
    if X % 10 == 0:
        print(X // 10 )
    else:
        print(X // 10 + 1)

# Another way to do it
from math import ceil
N = int(input())
for i in range(N):
    X = int(input())
    one_bag = ceil(X // 10)
    print(int(one_bag))
