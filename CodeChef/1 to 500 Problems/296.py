'''
Total Prize Money
-----------------
-> In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
-> Top 10 participants receive rupees X each.
-> Participants with rank 11 to 100 (both inclusive) receive rupees Y each.
-> Find the total prize money over all the contestants.

Input Format
--------------
-> First line will contain T, number of test cases. Then the test cases follow.
-> Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.

Output Format
-------------
-> For each test case, output the total prize money over all the contestants.

Sample 

input                   output

4
1000 100                19000
1000 1000               100000
80 1                    890
400 30                  6700
'''
 # Answer
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    total_prize = 10 * A  + 90 * B 
    print(total_prize)

#  another way 
N = int(input())
for i in range(N):
    A , B = map(int, input().split())
    print(10 * A + 90 * B)