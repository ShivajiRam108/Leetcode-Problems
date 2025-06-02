'''
Self Defence Training
----------------------
-> After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin.
-> The aim this time is to equip women with shaolin self-defence techniques.
-> The only condition for a woman to be eligible for the special training is that she must be between 10 and 60 years of age, inclusive of both 10 and 60.
-> Given the ages of N women in his village, please help San Te find out how many of them are eligible for the special training.

Input Format
-------------
-> The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
-> The first line of each test case contains a single integer N, the number of women.
-> The second line of each test case contains N space-separated integers A1 , A2 , .... An , the ages of the women.

Output Format
-------------
-> For each test case, output in a single line the number of women eligible for self-defence training.

Sample:-

input                   output

3
3
15 23 65                    2
3
15 62 16                    2
2
35 9                        1
'''
# Answer 
N = int(input())
for i in range(N):
    A  = int(input())
    Age = list(map(int, input().split()))
    count = 0
    for j in Age:
        if 10 <= j <= 60:
            count += 1
    print(count)