'''
Clear Day
-----------
-> Chef classifies a day to be either rainy, cloudy, or clear.

-> In a particular week, Chef finds X days to be rainy and Y days to be cloudy.
-> Find the number of clear days in the week.

Input Format
------------------
-> The first and only line of input will contain two space-separated integers X and 
    Y, denoting the number of rainy and cloudy days in the week.

Output Format
---------------
-> Output the number of clear days in the week.
'''

# Answer
a,b = map(int,input().split())
res = 7
if a + b == res:
    print("0")
else:
    print(res-(a+b))