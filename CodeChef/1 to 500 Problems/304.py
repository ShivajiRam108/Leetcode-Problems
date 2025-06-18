'''
Four Tickets
--------------
-> Four friends want to attend a concert. Each ticket costs X rupees.
-> They have decided to go to the concert if and only if the total cost of the tickets does not exceed 1000 rupees.
-> Determine whether they will be going to the concert or not.

Input Format
-------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single integer X, the cost of each ticket.

Output Format
--------------
-> For each test case, output YES if they will be going to the concert, NO otherwise.
-> You can print each character in uppercase or lowercase. For example, the strings YES, yes, Yes, and yES, are all considered identical.

Sample:-

input                       output

4
100                           YES
500                           NO
250                           YES
1000                          NO

'''
# Answer

N = int(input())
for i in range(N):
    A = int(input())
    res = A * 4 
    if res > 1000:
        print("NO")
    else:
        print("YES")