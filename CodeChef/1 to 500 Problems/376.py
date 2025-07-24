'''
Car Trip
--------
-> Chef rented a car for a day. Usually, the cost of the car is Rs 10 per km. 
-> However, since Chef has booked the car for the whole day, he needs to pay for at least 300 kms even if the car runs less than 300 kms.
-> If the car ran X kms, determine the cost Chef needs to pay.

Input Format
------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single integer X - denoting the number of kms Chef travelled.

Output Format
--------------
-> For each test case, output the cost Chef needs to pay.

Sample:- 

input                     output 
5
800                        8000
3                          3000
299                        3000
301                        3010
300                        3000
'''

# Answer

N = int(input())
for i in range(N):
    X = int(input())
    if X < 300:
        print(3000)
    else:
        print(X * 10)