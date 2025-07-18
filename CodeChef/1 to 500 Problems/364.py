'''
Time Complexity
----------------
-> A sorting algorithm A is said to have more time complexity than a sorting algorithm 
-> B if it uses more number of comparisons for sorting the same array than algorithm B.
-> Given that algorithm A uses X comparisons to sort an array and algorithm B uses Y comparisons to sort the same array, 
-> find whether algorithm A has more time complexity.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers X and Y — the number of comparisons used by algorithms
->  A and B to sort the array respectively.

Output Format
--------------
-> For each test case, output on a new line, YES, if the algorithm A has more time complexity than B and NO otherwise.
-> You may print each character of the string in uppercase or lowercase
->  (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Sample :- 

input                   output 

4
9 9                      No
15 7                     YeS
10 19                    No
21 20                    Yes
'''

# Answer 

N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    if X > Y :
        print("YES")
    else:
        print("NO")