'''
Lucky Seven
-------------------
-> Chef considers the number 7 lucky. As a result, he believes that the 
-> 7-th letter he sees on a day is his lucky letter of the day.

-> You are given a string S of length 10, denoting the first 10 letters Chef saw today.
-> What is Chef's lucky letter?

Input Format
-----------------
=> The only line of input contains a string S, of length 10.
Output Format
-------------------
=> Print a single character: Chef's lucky letter .

sample :-
input                    output
proceeding                  d
outofsight                  i
'''

# Answer 
# he is asking only index.
n = input()
print(n[6])