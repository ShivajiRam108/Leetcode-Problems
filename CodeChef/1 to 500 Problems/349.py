'''
Fever
-------
-> Chef is not feeling well today. He measured his body temperature using a thermometer and it came out to be X °F.
-> A person is said to have fever if his body temperature is strictly greater than 98 °F.
-> Determine if Chef has fever or not.

Input Format
-------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains one integer X - the body temperature of Chef in °F.

Output Format
--------------
-> For each test case, output YES if Chef has fever. Otherwise, output NO.
-> You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

Sample :- 

input               output
98                   No
99                   Yes
100                  Yes
96                   No


'''

# Answer 

N = int(input())
for _ in range(N):  
    X = int(input())
    if X > 98:
        print("Yes")
    else:
        print("No")
    
