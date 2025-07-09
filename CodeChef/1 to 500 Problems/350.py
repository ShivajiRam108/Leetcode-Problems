'''
Sleep deprivation
------------------
-> A person is said to be sleep deprived if he slept strictly less than 7 hours in a day.
-> Chef was only able to sleep X hours yesterday. Determine if he is sleep deprived or not.

Input Format
----------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains one integer X — the number of hours Chef slept.

Output Format
---------------
-> For each test case, output YES if Chef is sleep-deprived. Otherwise, output NO.
-> You may print each character of YES and NO in uppercase or lowercase
->  (for example, yes, yEs, Yes will be considered identical).

Sample :- 

input               output
3
4                    Yes
7                    No
10                   No
'''

# Answer

N = int(input())
for i in range(N):
    X = int(input())
    if X  < 7:
        print("Yes")
    else:
        print("NO")

  