'''
Tom and Jerry Chase
--------------------
-> In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
-> Jerry is running at a speed of X metres per second while Tom is chasing him at a speed of Y metres per second.
-> Determine whether Tom will be able to catch Jerry.

=> Note that initially Jerry is not at the same position as Tom.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of two space-separated integers X and Y — the speeds of Jerry and Tom respectively.

Output Format
-------------
-> For each test case, output on a new line, YES, if Tom will be able to catch Jerry. Otherwise, output NO.
-> You can print each character in uppercase or lowercase. For example NO, no, No, and nO are all considered the same.

Sample 

input                  output
4
2 3                      YES
4 1                      NO
1 1                      NO
3 5                      YES
'''
#Answer
N = int(input())
for i in range(N):
    A , B = map(int, input().split())
    if B > A:
        print("YES")
    else:
        print("NO")
#Time Complexity: O(N)
#Space Complexity: O(1)

# (Or)

# Alternative Solution
N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    print("YES" if Y > X else "NO")

#Time Complexity: O(N)
#Space Complexity: O(1)