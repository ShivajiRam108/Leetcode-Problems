'''
Chef gives Party
------------------
-> Chef wants to give a burger party to all his N friends i.e. he wants to buy one burger for each of his friends.
-> The cost of each burger is X rupees while Chef has a total of K rupees.
-> Determine whether he has enough money to buy a burger for each of his friends or not.

Input Format
---------------
-> The first line contains a single integer T - the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains the three integers N, X, and K -
->  the number of Chef's friends, the cost of each burger, and the total money Chef has, respectively.

Output Format
-------------
-> For each test case, output YES if the Chef can give a party to all his N friends. Otherwise, output NO.
-> You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).


Sample:- 

input                   output
4
5 10 70                   YES
5 10 40                   NO
10 40 400                 YES
14 14 150                 NO
'''

# Answer

N = int(input())
for i in range(N):
    X, Y , Z = map(int, input().split())
    res = X * Y 
    if res <= Z:
        print("YES")
    else:
        print("NO")
        