'''
Off By One
-------------
-> You just bought a new calculator, but it seems to have a small problem: all its results have an extra 1 appended to the end.
-> For example, if you ask it for 3 + 5, it'll print 81, and 4 + 12 will result in 161.

=> Given A and B, can you predict what the calculator will print when you ask it for + B A+B?

Input Format
---------------------
-> The first and only line of input will contain two space-separated integers A and B.

Output Format
-------------
-> Print a single integer: the calculator's output when you enter + BA+B into it.

sample:-

input                   output 

3 5                       81
4 12                      161
'''

# Answer:- 
a , b = map(int, input())
res = (10 * (a + b) + 1)
print(res)