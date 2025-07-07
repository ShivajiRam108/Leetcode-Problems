'''
Air Quality Index
------------------
-> In the light of G-20 summit, government has decided to keep the average air quality index (AQI) strictly below 100.
-> On some random day, Chef measures the AQI and found the value to be X.
-> Find whether the government was able to keep the AQI within limits.

Input Format
-------------
-> The input consists of an integer X — the AQI Chef measured.

Output Format
--------------
-> Output YES, if the government was able to keep the AQI within limits and NO otherwise.
-> You may print each character of the string in uppercase or lowercase
->  (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Sample :-

input               output 
50                    Yes
100                   No
99                    Yes

'''
# Answer
N = int(input())
if N < 100:
    print("Yes")
else:
    print("No")