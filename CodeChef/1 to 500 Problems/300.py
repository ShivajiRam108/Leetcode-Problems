'''
Ageing
----------
-> Chef's current age is 20 years, while Chefina's current age is 10 years.
-> Determine Chefina's age when Chef will be X years old.

=> Note: Assume that Chef and Chefina were born on same day and same month (just different year).

Input Format
============
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single integer X, the age of Chef.

Output Format
-------------
-> For each test case, output Chefina's age when Chef will be X years old.

Sample :-

input                   output

4
25                        15
36                        26
50                        40
44                        34
'''

#Answer
N = int(input())
for i in range(N):
    X = int(input())
    print(X - 10)
