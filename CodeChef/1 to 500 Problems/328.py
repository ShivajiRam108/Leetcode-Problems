'''
Rain in Chefland
------------------
-> In Chefland, precipitation is measured using a rain gauge in millimetre per hour.
-> Chef categorises rainfall as:

-> LIGHT, if rainfall is less than 3 millimetre per hour.
-> MODERATE, if rainfall is greater than equal to 3 millimetre per hour and less than 7 millimetre per hour.
-> HEAVY if rainfall is greater than equal to 7 millimetre per hour.
-> Given that it rains at X millimetre per hour on a day, find whether the rain is LIGHT, MODERATE, or HEAVY.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single integer X — the rate of rainfall in millimetre per hour.

Output Format
--------------
-> For each test case, output on a new line, whether the rain is LIGHT, MODERATE, or HEAVY.
-> You may print each character in lowercase or uppercase. For example, LIGHT, light, Light, and liGHT, are all identical.

Sample :-

input                   output 

4
1                       LIGHT
20                      HEAVY
3                       MODERATE
7                       HEAVY
'''

# Answer

N = int(input())
for i in range(N):
    X = int(input())
    if X < 3:
        print("LIGHT")
    elif X < 7:
        print("MODERATE")
    else:
        print("HEAVY")

        