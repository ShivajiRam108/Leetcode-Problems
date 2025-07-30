'''
The Gift
--------
-> Om has X rupees. He wants to gift a laptop worth N rupees to his girlfriend.
-> We know that Om is the technical secretary of IIIT-A and has access to the Gymkhana funds of IIIT-A. 
-> Currently there are M rupees in the fund and Om can use the fund as much as he wants.
-> Find whether Om can gift his girlfriend a new laptop.

Input Format
-------------
-> The first and only line of input contains three space-separated integers X, N, and M — the 
-> amount Om has, the price of the laptop, and the amount present in the Gymkhana fund respectively.

Output Format
--------------
-> For each input, output YES if Om can buy the laptop and NO otherwise.
-> You may print each character in uppercase or lowercase. For example YES, Yes, yes, and yES are all considered the same.

Sample:- 

input                      output
5 10 15                     Yes
4 50 7                      No
'''

# Answer
X, Y, Z = map(int, input().split())
if X + Z >= Y:
    print("Yes")
else:
    print("No")
    