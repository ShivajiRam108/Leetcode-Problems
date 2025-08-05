'''
Height of Rationals
--------------------
-> In a recent breakthrough in mathematics, the proof utilized a concept called Height.
-> Consider a fraction b a. Its Height is defined as the maximum of its numerator and denominator. 
-> So, for example, the Height of 19 3 would be 19, and the Height of 4 27 would be 27.
-> Given a and b, find the Height of b a.

Input Format
-------------
-> The only line of input contains two integers, a and b.

Output Format
--------------
-> Output a single integer, which is the Height of a b.

Sample:- 

input               output 
3 19                  19
27 4                  27
50 10                 50
​
'''

# Answer
X , Y = map(int,input().split())
print(max(X, Y))