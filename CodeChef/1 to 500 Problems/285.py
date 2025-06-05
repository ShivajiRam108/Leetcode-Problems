'''
2000
-----------
-> Chef had collected N notes of Rs. 2000 to pay his total college fees. However, the government banned Rs. 2000 notes.
-> Chef wants to pay the same amount using Rs. 500 notes only. Find the number of notes Chef needs.

Input Format
-------------
-> Each test case consists of a single integer N - the number of notes of Rs. 2000 that Chef has collected.

Output Format
------------
-> Output a single integer - the number of Rs. 500 notes needed.

Sample:-

Input               output

4                       16
10                      40
'''

# Answer
N = int(input())
convart_two_to_five_notes = N * 4
print(convart_two_to_five_notes)