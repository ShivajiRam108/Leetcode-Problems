'''
Masterchef finals
--------------------

-> Chef has been working hard to compete in MasterChef.He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals.
-> Check whether Chef made it to the top 10 or not?

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of one integers X — the current rank of Chef.

Output Format
-------------
-> For each test case, output on a new line, YES, if Chef made it to the top 10 and NO otherwise.
-> Each character of the output may be printed in either uppercase or lowercase. That is, the strings NO, no, nO, and No will be treated as equivalent.

sample:- 

input               output 
4 
15                    No
10                    Yes
1                     Yse
50                    No

'''

# Answer 

n = int(input())
for i in range(n):
    a = int(input())
    if a <= 10:
        print("Yse")
    else:
        print("No")