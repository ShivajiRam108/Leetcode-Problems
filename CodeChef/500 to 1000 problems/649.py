'''
Mario and Transformation
-----------------------------

Mario transforms each time he eats a mushroom as follows:

1. If he is currently small, he turns normal.
2. If he is currently normal, he turns huge.
3. If he is currently huge, he turns small.

Given that Mario was initially normal, find his size after eating  X mushrooms.

Input Format
--------------
1. The first line of input will contain one integer T, the number of test cases. Then the test cases follow.
2. Each test case contains a single line of input, containing one integer X.

Output Format
---------------
-> For each test case, output in a single line Mario's size after eating X mushrooms.

Print:
-----------

NORMAL, if his final size is normal.
HUGE, if his final size is huge.
SMALL, if his final size is small.


sample  :-
input                         output
3
2                               SMALL
4                               HUGE
12                              NORMAL

'''

# Answer :- 

n = int(input())
res = ["NORMAL" , "HUGE","SMALL" ]
for i in range(n):
    a = int(input())
    final = res[a % 3]
    print(final)