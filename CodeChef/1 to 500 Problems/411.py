'''
Is it hot or cold
------------------
-> Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. 
-> You are given the temperature C, find whether the climate is HOT or COLD.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> The first and only line of each test case contains a single integer, the temperature C.

Output Format
--------------
-> For each test case, print on a new line whether the climate is HOT or COLD.
-> You may print each character of the string in either uppercase or lowercase
->  (for example, the strings hOt, hot, Hot, and HOT will all be treated as identical).

Sample:- 

input           output
2 
20               HOT
16               COLD
'''

# Answer

N = int(input())
for i in range(N):
    X = int(input())
    if X > 20:
        print("HOT")
    else:
        print("COLD")