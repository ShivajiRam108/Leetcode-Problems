'''
Fill Candies
-------------
-> Chef received N candies on his birthday. He wants to put these candies in some bags. 
-> A bag has K pockets and each pocket can hold at most M candies.
-> Find the minimum number of bags Chef needs so that he can put every candy into a bag.

Input Format
--------------
-> The first line of input will contain a single integer T, denoting the number of test cases.
-> Each test case consists of a single line containing three space-separated integers ,K ,MN,K,M.

Output Format
--------------
-> For each test case, print the minimum number of bags Chef needs so that he can put all the candies in one of the bags.

sample:-

input                   output
4
6 2 3                     1
3 1 2                     2
8 4 1                     2
25 4 2                    4

'''

# Answer:-
import math
n = int(input())
for i in range(n):
    a , b , c= map(int, input().split())
    one_bag_cap = b * c
    need_bags = math.ceil(a / one_bag_cap)
    print(need_bags)