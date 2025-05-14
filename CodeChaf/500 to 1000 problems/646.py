'''
Finding Shoes
Chef has 
N friends. Chef promised that he would gift a pair of shoes (consisting of one left shoe and one right shoe) to each of his 
N friends. Chef was about to go to the marketplace to buy shoes, but he suddenly remembers that he already had 
M left shoes.

What is the minimum number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his 

N friends?

input :           output:         
3 
2 4                 2
6 0                 12
4 3                 5

'''

#  Answer
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if b  >= a:
        print(a)
    else:
        print(2 * a - b)