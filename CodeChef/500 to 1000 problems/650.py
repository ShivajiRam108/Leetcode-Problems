'''
Mario and Bullet
------------------
-> Mario's bullet moves at X pixels per frame. He wishes to shoot a goomba standing Y pixels away from him. The goomba does not move.
-> Find the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least Z seconds from now.

Input Format
-------------
-> The first line of input will contain an integer T, the number of test cases. Then the test cases follow.
-> Each test case consists of a single line of input, containing three space-separated integers 
=> X,Y, and Z.

Output Format
----------------
-> For each test case, output in a single line the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least Z seconds from now.


input               output 
3 
3 3 5                   4
2 4 1                   0 
3 12 8                  4

'''

#  Answer

n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    travel_time = b  //  a
    wait_time = max(0, c - travel_time)
    print(wait_time)
   