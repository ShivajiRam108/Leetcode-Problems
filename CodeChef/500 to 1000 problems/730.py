'''
Second Largest
---------------
Three numbers A, B and C are the inputs. Write a program to find second largest among them.

Input Format
---------------
The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

Output Format
--------------
For each test case, display the second largest among A, B and C, in a new line.

Sample 

input             output

3 
120 11 400          120
10213 312 10        312
10 3 450            10
'''
# Answer using simple if-else conditions

N = int(input())
for i in range(N):
    A, B , C = map(int, input().split())
    if A > B and A > C:
        if B > C:
            print(B)
        else:
            print(C)
    elif B > A and B > C:
        if A > C:
            print(A)
        else:
            print(C)
    else:
        if A > B:
            print(A)
        else:
            print(B)

#    (Or) 
        
'''Alternate solution using sorted function'''
N = int(input())
for i in range(N):        
    A, B , C = map(int, input().split())
    print(sorted([A, B, C])[-2])  # Sort the numbers and get the second largest

'''Alternate solution using max and min'''
N = int(input())
for i in range(N):
    A, B , C = map(int, input().split())
    second_largest = max(min(A, B), min(max(A, B), C))
    print(second_largest)  # Find the second largest using max and min
