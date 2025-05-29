'''
Chef and his Apps
------------------
-> Chef's phone has a total storage of S MB. Also, Chef has 2 apps already installed on his phone which occupy X MB and Y MB respectively.
-> He wants to install another app on his phone whose memory requirement is Z MB. 
-> For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

Input Format
-------------
-> The first line contains a single integer T — the number of test cases. Then the test cases follow.
-> The first and only line of each test case contains four integers ,X,Y, S,X,Y and Z
-> Z — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.

Output Format
-------------
-> For each test case, output the minimum number of apps Chef has to delete from his phone so that he can install the third app.

sample:-

input                   output

4
10 1 2 3                0
9 4 5 1                 1
15 5 10 15              2
100 20 30 75            1
'''

# Answer:-
n = int(input())
for i in range(n):
    A , B , C ,D = map(int,input().split())
    X = B + C 
    res = A - X 
    if res >= D:
        print(0)
    elif res + max(B , C) >= D:
        print(1)
    else:
        print(2)
