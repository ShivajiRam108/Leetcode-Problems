'''
Chef and Masks
---------------
-> Chef is shopping for masks. In the shop, he encounters 2 types of masks:
-> Disposable Masks — cost X but last only 1 day.Cloth Masks — cost Y but last 10 days.
-> Chef wants to buy masks to last him 100 days. He will buy the masks which cost him the least. 
-> In case there is a tie in terms of cost, Chef will be eco-friendly and choose the cloth masks.
-> Which type of mask will Chef choose?

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
-> Each test case consists of a single line of input, containing two space-separated integers X,Y.

Output Format
--------------
-> For each test case, if Chef buys the cloth masks print CLOTH, otherwise print DISPOSABLE.
-> You may print each character of the string in uppercase or lowercase 
-> (for example, the strings cloth, clOTh, cLoTH, and CLOTH will all be treated as identical).

Sample:- 

input             output
4 
10 100             Cloth
9 100              Disposable
88 99              Cloth
1 11               Disposable
'''


N = int(input())
for i in range(N):
    X , Y = map(int, input().split())
    if X * 100 < Y * 10:
        print("DISPOSABLE")
    else:
        print("CLOTH")